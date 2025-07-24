import pytest
import io
from pilotlog.export_csv import export_aircraft_to_csv, export_flights_to_csv
from pilotlog.models import Aircraft, Flight, Pilot


@pytest.mark.django_db
def test_export_aircraft_to_csv(tmp_path):
    # Create a sample Aircraft
    aircraft = Aircraft.objects.create(
        guid="00000000-0000-0000-0000-000000000367",
        fin="",
        sea=False,
        tmg=False,
        efis=False,
        fnpt=0,
        make="Cessna",
        run2=False,
        aircraft_class=5,
        model="C150",
        power=1,
        seats=2,
        active=True,
        kg5700=False,
        rating="",
        company="Other",
        complex=False,
        cond_log=69,
        fav_list=False,
        category=1,
        high_perf=False,
        sub_model="",
        aerobatic=False,
        ref_search="PHALI",
        reference="PH-ALI",
        tailwheel=False,
        default_app=0,
        default_log=2,
        default_ops=0,
        device_code=1,
        default_launch=0,
        record_modified=1616320991,
    )
    # Export to a string buffer
    buf = io.StringIO()
    export_aircraft_to_csv(buf)
    csv_content = buf.getvalue()
    buf.close()

    # Check that the static headers are present
    assert "ForeFlight Logbook Import" in csv_content
    assert "Aircraft Table" in csv_content
    assert (
        "AircraftID,EquipmentType,TypeCode,Year,Make,Model,Category,Class,GearType,EngineType,Complex,HighPerformance,Pressurized,TAA"
        in csv_content
    )

    # Check that the aircraft data row is present
    assert aircraft.guid in csv_content
    assert "Cessna" in csv_content
    assert "C150" in csv_content
    # Check that the number of columns matches the template
    data_row = [row for row in csv_content.splitlines() if "Cessna" in row][0]
    assert len(data_row.split(",")) >= 14  # At least as many as the template columns


@pytest.mark.django_db
def test_export_flights_to_csv(tmp_path):
    # Create a sample Aircraft
    aircraft = Aircraft.objects.create(
        guid="00000000-0000-0000-0000-000000000367",
        fin="",
        sea=False,
        tmg=False,
        efis=False,
        fnpt=0,
        make="Cessna",
        run2=False,
        aircraft_class=5,
        model="C150",
        power=1,
        seats=2,
        active=True,
        kg5700=False,
        rating="",
        company="Other",
        complex=False,
        cond_log=69,
        fav_list=False,
        category=1,
        high_perf=False,
        sub_model="",
        aerobatic=False,
        ref_search="PHALI",
        reference="PH-ALI",
        tailwheel=False,
        default_app=0,
        default_log=2,
        default_ops=0,
        device_code=1,
        default_launch=0,
        record_modified=1616320991,
    )
    # Create a sample Flight
    flight = Flight.objects.create(
        guid="FF8CC30B-07F3-4C4C-9602-F93A2A726829",
        aircraft=aircraft,
        pf=True,
        pax=2,
        fuel=100,
        deice=False,
        route="KJFK-KLGA",
        to_day=1,
        min_u1=10,
        min_u2=20,
        min_u3=30,
        min_u4=40,
        min_xc=50,
        arr_rwy="04",
        dep_rwy="22",
        ldg_day=1,
        lift_sw=0,
        report="",
        tag_ops="",
        to_edit=False,
        min_air=0,
        min_cop=0,
        min_ifr=0,
        min_imt=0,
        min_pic=0,
        min_rel=0,
        min_sfr=0,
        hobbs_in=0,
        holding=0,
        pairing="",
        remarks="",
        sign_box=0,
        to_night=0,
        user_num=0,
        min_dual=0,
        min_exam=0,
        crew_list="",
        fuel_used=0,
        hobbs_out=0,
        ldg_night=0,
        next_page=False,
        tag_delay="",
        training="",
        user_bool=False,
        user_text="",
        min_instr=0,
        min_night=0,
        min_picus=0,
        min_total=0,
        arr_offset=0,
        dep_offset=0,
        tag_launch="",
        tag_lesson="",
        to_time_utc=0,
        arr_time_utc=0,
        base_offset=0,
        dep_time_utc=0,
        ldg_time_utc=0,
        fuel_planned=0,
        next_summary=False,
        tag_approach="",
        arr_time_sched=0,
        dep_time_sched=0,
        flight_number="",
        flight_search="",
        record_modified=1681419475,
    )
    # Export to a string buffer
    buf = io.StringIO()
    export_flights_to_csv(buf)
    csv_content = buf.getvalue()
    buf.close()

    # Check that the static headers are present
    assert "Flights Table" in csv_content
    assert (
        "Date,AircraftID,From,To,Route,TimeOut,TimeOff,TimeOn,TimeIn,OnDuty,OffDuty,TotalTime,PIC,SIC,Night,Solo,CrossCountry,NVG,NVGOps,Distance,DayTakeoffs,DayLandingsFullStop,NightTakeoffs,NightLandingsFullStop,AllLandings,ActualInstrument,SimulatedInstrument,HobbsStart,HobbsEnd,TachStart,TachEnd,Holds,Approach1,Approach2,Approach3,Approach4,Approach5,Approach6,DualGiven,DualReceived,SimulatedFlight,GroundTraining,InstructorName,InstructorComments,Person1,Person2,Person3,Person4,Person5,Person6,FlightReview,Checkride,IPC,NVGProficiency,FAA6158,TextCustomFieldName,NumericCustomFieldName,HoursCustomFieldName,CounterCustomFieldName,DateCustomFieldName,DateTimeCustomFieldName,ToggleCustomFieldName,PilotComments"
        in csv_content
    )

    # Check that the flight data row is present
    assert "KJFK-KLGA" in csv_content
    assert "00000000-0000-0000-0000-000000000367" in csv_content  # AircraftID
    # Check that the number of columns matches the template
    data_row = [row for row in csv_content.splitlines() if "KJFK-KLGA" in row][0]
    assert len(data_row.split(",")) >= 63  # At least as many as the template columns


@pytest.mark.django_db
def test_export_with_actual_data():
    """Test CSV export with real Aircraft and Flight data"""
    # Create test data
    aircraft = Aircraft.objects.create(
        guid='12345678-1234-5678-9abc-123456789008',
        make='Cessna',
        model='C172',
        aircraft_class=1,
        power=1,
        seats=4,
        company='Flight School',
        cond_log=50,
        category=1,
        ref_search='C172',
        reference='N12345',
        complex=False,
        high_perf=False,
        record_modified=1234567890
    )
    
    pilot = Pilot.objects.create(
        guid='12345678-1234-5678-9abc-123456789009',
        pilot_name='Jane Pilot',
        pilot_ref='P002',
        company='Flight School',
        pilot_search='Jane Pilot',
        record_modified=1234567890
    )
    
    flight = Flight.objects.create(
        guid='12345678-1234-5678-9abc-123456789010',
        aircraft=aircraft,
        p1=pilot,
        route='KBOS-KPVD',
        pf=True,
        min_total=180,
        min_pic=180,
        pax=1,
        flight_search='EXPORT-TEST-SEARCH',
        record_modified=1234567890
    )
    
    # Test aircraft export
    buf = io.StringIO()
    export_aircraft_to_csv(buf)
    aircraft_csv = buf.getvalue()
    buf.close()
    
    assert 'Cessna' in aircraft_csv
    assert 'C172' in aircraft_csv
    assert '12345678-1234-5678-9abc-123456789008' in aircraft_csv
    
    # Test flight export
    buf = io.StringIO()
    export_flights_to_csv(buf)
    flight_csv = buf.getvalue()
    buf.close()
    
    assert '12345678-1234-5678-9abc-123456789008' in flight_csv  # Should contain aircraft ID
    assert 'KBOS-KPVD' in flight_csv
