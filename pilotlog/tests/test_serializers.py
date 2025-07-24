import pytest
from pilotlog.serializers.import_serializers import (
    AircraftImportSerializer,
    FlightImportSerializer,
)
import io
from pilotlog.export_csv import export_aircraft_to_csv, export_flights_to_csv
from pilotlog.models import Aircraft, Flight, Pilot, Airfield
from pilotlog.serializers.export_serializers import (
    AircraftExportSerializer,
)


@pytest.mark.django_db
def test_aircraft_import_serializer_wrong_type():
    """Test that serializer ignores fields with wrong types (current behavior)"""
    payload = {
        "AircraftCode": "00000000-0000-0000-0000-000000000367",
        "FNPT": "not_an_int",  # This should be ignored
        "Sea": "not_a_bool",  # This should be ignored
        "Make": "Cessna",  # This should be kept but currently isn't
        "Class": 5,  # This should work
        "Fin": "",  # Required, allow_blank
        "Model": "",  # allow_blank
        "Rating": "",  # allow_blank
        "Company": "",  # allow_blank
        "SubModel": "",  # allow_blank
        "RefSearch": "",  # allow_blank
        "Reference": "",  # allow_blank
        "Record_Modified": 1234567890,  # Required
    }
    serializer = AircraftImportSerializer(data=payload)
    assert not serializer.is_valid() or "FNPT" not in serializer.validated_data
    # Should fail is_valid due to wrong type, or FNPT should be missing from validated_data if is_valid passes


@pytest.mark.django_db
def test_flight_import_serializer_wrong_type():
    """Test that serializer properly validates field types with PascalCase fields"""
    payload = {
        "FlightCode": "FF8CC30B-07F3-4C4C-9602-F93A2A726829",
        "PF": "not_a_bool",  # This should cause validation error
        "Pax": "not_an_int",  # This should cause validation error
        "Route": "KJFK-KLGA",  # This should be valid
    }
    serializer = FlightImportSerializer(data=payload)
    # Now that we use PascalCase fields, validation should fail for wrong types
    assert not serializer.is_valid()
    assert "PF" in serializer.errors
    assert "Pax" in serializer.errors
    # Route should not have errors since it's a valid string
    assert "Route" not in serializer.errors


@pytest.mark.django_db
def test_aircraft_import_with_minimal_data():
    """Test Aircraft import with minimal required fields only"""
    payload = {
        "AircraftCode": "12345678-1234-5678-9abc-123456789012",
        "Make": "Cessna",
        "Model": "C172",
        "Class": 2,
        "Company": "Flight School",
        "CondLog": 100,
        "Category": 1,
        "RefSearch": "C172",
        "Reference": "N12345",
        "Record_Modified": 1234567890,
    }
    serializer = AircraftImportSerializer(data=payload)
    assert serializer.is_valid(), serializer.errors
    aircraft = serializer.save()
    assert str(aircraft.guid) == "12345678-1234-5678-9abc-123456789012"
    assert aircraft.aircraft_class == 2
    assert aircraft.record_modified == 1234567890


@pytest.mark.django_db
def test_flight_import_with_foreign_keys():
    """Test Flight import with foreign key relationships"""
    # Create related objects first
    aircraft = Aircraft.objects.create(
        guid="12345678-1234-5678-9abc-123456789001",
        make="Boeing",
        model="737",
        aircraft_class=1,
        power=2,
        seats=150,
        company="Airline",
        cond_log=100,
        category=1,
        ref_search="B737",
        reference="N12345",
        record_modified=1234567890,
    )
    pilot = Pilot.objects.create(
        guid="12345678-1234-5678-9abc-123456789002",
        pilot_name="John Doe",
        pilot_ref="P001",
        company="Airline",
        pilot_search="John Doe",
        record_modified=1234567890,
    )
    airfield = Airfield.objects.create(
        guid="12345678-1234-5678-9abc-123456789003",
        af_name="Test Airport",
        af_icao="TEST",
        af_iata="TST",
        af_cat=1,
        tz_code=1,
        latitude=123456,
        longitude=654321,
        af_country=1,
        record_modified=1234567890,
    )

    payload = {
        "FlightCode": "12345678-1234-5678-9abc-123456789004",
        "AircraftCode": "12345678-1234-5678-9abc-123456789001",
        "P1Code": "12345678-1234-5678-9abc-123456789002",
        "ArrCode": "12345678-1234-5678-9abc-123456789003",
        "DepCode": "12345678-1234-5678-9abc-123456789003",
        "Route": "TEST-TEST",
        "PF": True,
        "minTOTAL": 120,
        "FlightSearch": "TEST-FLIGHT-SEARCH",
    }
    serializer = FlightImportSerializer(data=payload)
    assert serializer.is_valid(), serializer.errors
    flight = serializer.save()

    assert str(flight.guid) == "12345678-1234-5678-9abc-123456789004"
    assert str(flight.aircraft.guid) == str(aircraft.guid)
    assert str(flight.p1.guid) == str(pilot.guid)
    assert str(flight.arr_airfield.guid) == str(airfield.guid)
    assert str(flight.dep_airfield.guid) == str(airfield.guid)
    assert flight.route == "TEST-TEST"
    assert flight.pf is True
    assert flight.min_total == 120


@pytest.mark.django_db
def test_flight_import_with_missing_foreign_keys():
    """Test Flight import when referenced objects don't exist"""
    payload = {
        "FlightCode": "12345678-1234-5678-9abc-123456789005",
        "AircraftCode": "12345678-1234-5678-9abc-000000000001",
        "P1Code": "12345678-1234-5678-9abc-000000000002",
        "ArrCode": "12345678-1234-5678-9abc-000000000003",
        "Route": "NOWHERE-SOMEWHERE",
        "FlightSearch": "MISSING-FK-SEARCH",
    }
    serializer = FlightImportSerializer(data=payload)
    assert serializer.is_valid(), serializer.errors
    flight = serializer.save()

    assert str(flight.guid) == "12345678-1234-5678-9abc-123456789005"
    assert flight.aircraft is None
    assert flight.p1 is None
    assert flight.arr_airfield is None
    assert flight.route == "NOWHERE-SOMEWHERE"


@pytest.mark.django_db
def test_export_with_actual_data():
    """Test CSV export with real Aircraft and Flight data"""
    # Create test data
    aircraft = Aircraft.objects.create(
        guid="12345678-1234-5678-9abc-123456789008",
        make="Cessna",
        model="C172",
        aircraft_class=1,
        power=1,
        seats=4,
        company="Flight School",
        cond_log=50,
        category=1,
        ref_search="C172",
        reference="N12345",
        complex=False,
        high_perf=False,
        record_modified=1234567890,
    )

    pilot = Pilot.objects.create(
        guid="12345678-1234-5678-9abc-123456789009",
        pilot_name="Jane Pilot",
        pilot_ref="P002",
        company="Flight School",
        pilot_search="Jane Pilot",
        record_modified=1234567890,
    )

    Flight.objects.create(
        guid="12345678-1234-5678-9abc-123456789010",
        aircraft=aircraft,
        p1=pilot,
        route="KBOS-KPVD",
        pf=True,
        min_total=180,
        min_pic=180,
        pax=1,
        flight_search="EXPORT-TEST-SEARCH",
        record_modified=1234567890,
    )

    # Test aircraft export
    buf = io.StringIO()
    export_aircraft_to_csv(buf)
    aircraft_csv = buf.getvalue()
    buf.close()

    assert "Cessna" in aircraft_csv
    assert "C172" in aircraft_csv
    assert "12345678-1234-5678-9abc-123456789008" in aircraft_csv

    # Test flight export
    buf = io.StringIO()
    export_flights_to_csv(buf)
    flight_csv = buf.getvalue()
    buf.close()

    assert (
        "12345678-1234-5678-9abc-123456789008" in flight_csv
    )  # Should contain aircraft ID
    assert "KBOS-KPVD" in flight_csv


@pytest.mark.django_db
def test_serializer_field_validation():
    """Test that serializers properly validate field types and constraints"""
    # Test Aircraft serializer validation
    invalid_aircraft = {
        "AircraftCode": "not-a-uuid-format",  # Invalid UUID
        "Class": "not-an-integer",  # Invalid integer
        "Power": -1,  # Potentially invalid value
    }
    serializer = AircraftImportSerializer(data=invalid_aircraft)
    assert not serializer.is_valid()
    assert "Class" in serializer.errors

    # Test Flight serializer validation
    invalid_flight = {
        "FlightCode": "",  # Empty required field
        "PF": "not-a-boolean",  # Invalid boolean
        "minTOTAL": "not-an-integer",  # Invalid integer
    }
    serializer = FlightImportSerializer(data=invalid_flight)
    assert not serializer.is_valid()
    assert "PF" in serializer.errors
    assert "minTOTAL" in serializer.errors


@pytest.mark.django_db
def test_export_serializer_output():
    """Test that export serializers produce expected output format"""
    aircraft = Aircraft.objects.create(
        guid="12345678-1234-5678-9abc-123456789011",
        make="Piper",
        model="PA-28",
        aircraft_class=2,
        power=1,
        seats=4,
        company="Flying Club",
        cond_log=25,
        category=1,
        ref_search="PA28",
        reference="N98765",
        complex=True,
        high_perf=False,
        record_modified=1234567890,
    )

    serializer = AircraftExportSerializer(aircraft)
    data = serializer.data

    assert data["AircraftID"] == "12345678-1234-5678-9abc-123456789011"
    assert data["Make"] == "Piper"
    assert data["Model"] == "PA-28"
    assert data["Class"] == 2
    assert data["Complex"] is True
    assert data["HighPerformance"] is False
    # Test that empty method fields return empty strings
    assert data["EquipmentType"] == ""
    assert data["Year"] == ""
