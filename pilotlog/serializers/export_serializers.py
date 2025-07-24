from .base_serializers import (
    DefaultEmptyMethodFieldMixin,
    BaseAircraftSerializer,
    BaseFlightSerializer,
)
from rest_framework import serializers


class AircraftExportSerializer(DefaultEmptyMethodFieldMixin, BaseAircraftSerializer):
    AircraftID = serializers.SerializerMethodField()
    EquipmentType = serializers.SerializerMethodField()
    TypeCode = serializers.SerializerMethodField()
    Year = serializers.SerializerMethodField()
    Make = serializers.CharField(source="make", allow_blank=True)
    Model = serializers.CharField(source="model", allow_blank=True)
    Category = serializers.SerializerMethodField()
    Class = serializers.IntegerField(source="aircraft_class")
    GearType = serializers.SerializerMethodField()
    EngineType = serializers.SerializerMethodField()
    Complex = serializers.BooleanField(source="complex")
    HighPerformance = serializers.BooleanField(source="high_perf")
    Pressurized = serializers.SerializerMethodField()
    TAA = serializers.SerializerMethodField()

    class Meta(BaseAircraftSerializer.Meta):
        fields = [
            "AircraftID",
            "EquipmentType",
            "TypeCode",
            "Year",
            "Make",
            "Model",
            "Category",
            "Class",
            "GearType",
            "EngineType",
            "Complex",
            "HighPerformance",
            "Pressurized",
            "TAA",
        ]

    def get_AircraftID(self, obj):
        return str(obj.guid)


class FlightExportSerializer(DefaultEmptyMethodFieldMixin, BaseFlightSerializer):
    Date = serializers.DateField(source="date_utc", format="%Y-%m-%d", required=False)
    AircraftID = serializers.SerializerMethodField()
    From = serializers.SerializerMethodField()
    To = serializers.SerializerMethodField()
    Route = serializers.CharField(source="route", allow_blank=True, required=False)
    TimeOut = serializers.SerializerMethodField()
    TimeOff = serializers.SerializerMethodField()
    TimeOn = serializers.SerializerMethodField()
    TimeIn = serializers.SerializerMethodField()
    OnDuty = serializers.SerializerMethodField()
    OffDuty = serializers.SerializerMethodField()
    TotalTime = serializers.SerializerMethodField()
    PIC = serializers.SerializerMethodField()
    SIC = serializers.SerializerMethodField()
    Night = serializers.SerializerMethodField()
    Solo = serializers.SerializerMethodField()
    CrossCountry = serializers.SerializerMethodField()
    NVG = serializers.SerializerMethodField()
    NVGOps = serializers.SerializerMethodField()
    Distance = serializers.SerializerMethodField()
    DayTakeoffs = serializers.SerializerMethodField()
    DayLandingsFullStop = serializers.SerializerMethodField()
    NightTakeoffs = serializers.SerializerMethodField()
    NightLandingsFullStop = serializers.SerializerMethodField()
    AllLandings = serializers.SerializerMethodField()
    ActualInstrument = serializers.SerializerMethodField()
    SimulatedInstrument = serializers.SerializerMethodField()
    HobbsStart = serializers.SerializerMethodField()
    HobbsEnd = serializers.SerializerMethodField()
    TachStart = serializers.SerializerMethodField()
    TachEnd = serializers.SerializerMethodField()
    Holds = serializers.SerializerMethodField()
    Approach1 = serializers.SerializerMethodField()
    Approach2 = serializers.SerializerMethodField()
    Approach3 = serializers.SerializerMethodField()
    Approach4 = serializers.SerializerMethodField()
    Approach5 = serializers.SerializerMethodField()
    Approach6 = serializers.SerializerMethodField()
    DualGiven = serializers.SerializerMethodField()
    DualReceived = serializers.SerializerMethodField()
    SimulatedFlight = serializers.SerializerMethodField()
    GroundTraining = serializers.SerializerMethodField()
    InstructorName = serializers.SerializerMethodField()
    InstructorComments = serializers.SerializerMethodField()
    Person1 = serializers.SerializerMethodField()
    Person2 = serializers.SerializerMethodField()
    Person3 = serializers.SerializerMethodField()
    Person4 = serializers.SerializerMethodField()
    Person5 = serializers.SerializerMethodField()
    Person6 = serializers.SerializerMethodField()
    FlightReview = serializers.SerializerMethodField()
    Checkride = serializers.SerializerMethodField()
    IPC = serializers.SerializerMethodField()
    NVGProficiency = serializers.SerializerMethodField()
    FAA6158 = serializers.SerializerMethodField()
    TextCustomFieldName = serializers.SerializerMethodField()
    NumericCustomFieldName = serializers.SerializerMethodField()
    HoursCustomFieldName = serializers.SerializerMethodField()
    CounterCustomFieldName = serializers.SerializerMethodField()
    DateCustomFieldName = serializers.SerializerMethodField()
    DateTimeCustomFieldName = serializers.SerializerMethodField()
    ToggleCustomFieldName = serializers.SerializerMethodField()
    PilotComments = serializers.SerializerMethodField()

    class Meta(BaseFlightSerializer.Meta):
        fields = [
            "Date",
            "AircraftID",
            "From",
            "To",
            "Route",
            "TimeOut",
            "TimeOff",
            "TimeOn",
            "TimeIn",
            "OnDuty",
            "OffDuty",
            "TotalTime",
            "PIC",
            "SIC",
            "Night",
            "Solo",
            "CrossCountry",
            "NVG",
            "NVGOps",
            "Distance",
            "DayTakeoffs",
            "DayLandingsFullStop",
            "NightTakeoffs",
            "NightLandingsFullStop",
            "AllLandings",
            "ActualInstrument",
            "SimulatedInstrument",
            "HobbsStart",
            "HobbsEnd",
            "TachStart",
            "TachEnd",
            "Holds",
            "Approach1",
            "Approach2",
            "Approach3",
            "Approach4",
            "Approach5",
            "Approach6",
            "DualGiven",
            "DualReceived",
            "SimulatedFlight",
            "GroundTraining",
            "InstructorName",
            "InstructorComments",
            "Person1",
            "Person2",
            "Person3",
            "Person4",
            "Person5",
            "Person6",
            "FlightReview",
            "Checkride",
            "IPC",
            "NVGProficiency",
            "FAA6158",
            "TextCustomFieldName",
            "NumericCustomFieldName",
            "HoursCustomFieldName",
            "CounterCustomFieldName",
            "DateCustomFieldName",
            "DateTimeCustomFieldName",
            "ToggleCustomFieldName",
            "PilotComments",
        ]

    def get_AircraftID(self, obj):
        return str(obj.aircraft.guid) if obj.aircraft else ""
