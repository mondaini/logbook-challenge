from .base_serializers import BaseAircraftSerializer, BaseFlightSerializer
from rest_framework import serializers
from ..models import Aircraft, Pilot, Airfield


class AircraftImportSerializer(BaseAircraftSerializer):
    AircraftCode = serializers.UUIDField(source="guid", required=True)
    Fin = serializers.CharField(source="fin", allow_blank=True, required=False)
    Sea = serializers.BooleanField(source="sea", required=False)
    TMG = serializers.BooleanField(source="tmg", required=False)
    Efis = serializers.BooleanField(source="efis", required=False)
    FNPT = serializers.IntegerField(source="fnpt", required=False)
    Make = serializers.CharField(source="make", allow_blank=True, required=False)
    Run2 = serializers.BooleanField(source="run2", required=False)
    Class = serializers.IntegerField(source="aircraft_class", required=True)
    Model = serializers.CharField(source="model", allow_blank=True, required=False)
    Power = serializers.IntegerField(source="power", required=False)
    Seats = serializers.IntegerField(source="seats", required=False)
    Active = serializers.BooleanField(source="active", required=False)
    Kg5700 = serializers.BooleanField(source="kg5700", required=False)
    Rating = serializers.CharField(source="rating", allow_blank=True, required=False)
    Company = serializers.CharField(source="company", allow_blank=True, required=False)
    Complex = serializers.BooleanField(source="complex", required=False)
    CondLog = serializers.IntegerField(source="cond_log", required=False)
    FavList = serializers.BooleanField(source="fav_list", required=False)
    Category = serializers.IntegerField(source="category", required=False)
    HighPerf = serializers.BooleanField(source="high_perf", required=False)
    SubModel = serializers.CharField(
        source="sub_model", allow_blank=True, required=False
    )
    Aerobatic = serializers.BooleanField(source="aerobatic", required=False)
    RefSearch = serializers.CharField(
        source="ref_search", allow_blank=True, required=False
    )
    Reference = serializers.CharField(
        source="reference", allow_blank=True, required=False
    )
    Tailwheel = serializers.BooleanField(source="tailwheel", required=False)
    DefaultApp = serializers.IntegerField(source="default_app", required=False)
    DefaultLog = serializers.IntegerField(source="default_log", required=False)
    DefaultOps = serializers.IntegerField(source="default_ops", required=False)
    DeviceCode = serializers.IntegerField(source="device_code", required=False)
    DefaultLaunch = serializers.IntegerField(source="default_launch", required=False)
    Record_Modified = serializers.IntegerField(source="record_modified", required=True)

    class Meta(BaseAircraftSerializer.Meta):
        fields = [
            "AircraftCode",
            "Fin",
            "Sea",
            "TMG",
            "Efis",
            "FNPT",
            "Make",
            "Run2",
            "Class",
            "Model",
            "Power",
            "Seats",
            "Active",
            "Kg5700",
            "Rating",
            "Company",
            "Complex",
            "CondLog",
            "FavList",
            "Category",
            "HighPerf",
            "SubModel",
            "Aerobatic",
            "RefSearch",
            "Reference",
            "Tailwheel",
            "DefaultApp",
            "DefaultLog",
            "DefaultOps",
            "DeviceCode",
            "DefaultLaunch",
            "Record_Modified",
        ]


class FlightImportSerializer(BaseFlightSerializer):
    FlightCode = serializers.CharField(source="guid", required=True)
    PF = serializers.BooleanField(source="pf", required=False)
    Pax = serializers.IntegerField(source="pax", required=False, allow_null=True)
    Fuel = serializers.IntegerField(source="fuel", required=False, allow_null=True)
    DeIce = serializers.BooleanField(source="deice", required=False)
    Route = serializers.CharField(source="route", required=False, allow_blank=True)
    ToDay = serializers.IntegerField(source="to_day", required=False, allow_null=True)
    minU1 = serializers.IntegerField(source="min_u1", required=False, allow_null=True)
    minU2 = serializers.IntegerField(source="min_u2", required=False, allow_null=True)
    minU3 = serializers.IntegerField(source="min_u3", required=False, allow_null=True)
    minU4 = serializers.IntegerField(source="min_u4", required=False, allow_null=True)
    minXC = serializers.IntegerField(source="min_xc", required=False, allow_null=True)
    ArrRwy = serializers.CharField(source="arr_rwy", required=False, allow_blank=True)
    DepRwy = serializers.CharField(source="dep_rwy", required=False, allow_blank=True)
    LdgDay = serializers.IntegerField(source="ldg_day", required=False, allow_null=True)
    LiftSW = serializers.IntegerField(source="lift_sw", required=False, allow_null=True)
    P1Code = serializers.CharField(required=False, allow_blank=True)
    P2Code = serializers.CharField(required=False, allow_blank=True)
    P3Code = serializers.CharField(required=False, allow_blank=True)
    P4Code = serializers.CharField(required=False, allow_blank=True)
    Report = serializers.CharField(source="report", required=False, allow_blank=True)
    TagOps = serializers.CharField(source="tag_ops", required=False, allow_blank=True)
    ToEdit = serializers.BooleanField(source="to_edit", required=False)
    minAIR = serializers.IntegerField(source="min_air", required=False, allow_null=True)
    minCOP = serializers.IntegerField(source="min_cop", required=False, allow_null=True)
    minIFR = serializers.IntegerField(source="min_ifr", required=False, allow_null=True)
    minIMT = serializers.IntegerField(source="min_imt", required=False, allow_null=True)
    minPIC = serializers.IntegerField(source="min_pic", required=False, allow_null=True)
    minREL = serializers.IntegerField(source="min_rel", required=False, allow_null=True)
    minSFR = serializers.IntegerField(source="min_sfr", required=False, allow_null=True)
    ArrCode = serializers.CharField(required=False, allow_blank=True)
    DateUTC = serializers.DateField(source="date_utc", required=False)
    DepCode = serializers.CharField(required=False, allow_blank=True)
    HobbsIn = serializers.IntegerField(
        source="hobbs_in", required=False, allow_null=True
    )
    Holding = serializers.IntegerField(
        source="holding", required=False, allow_null=True
    )
    Pairing = serializers.CharField(source="pairing", required=False, allow_blank=True)
    Remarks = serializers.CharField(source="remarks", required=False, allow_blank=True)
    SignBox = serializers.IntegerField(
        source="sign_box", required=False, allow_null=True
    )
    ToNight = serializers.IntegerField(
        source="to_night", required=False, allow_null=True
    )
    UserNum = serializers.IntegerField(
        source="user_num", required=False, allow_null=True
    )
    minDUAL = serializers.IntegerField(
        source="min_dual", required=False, allow_null=True
    )
    minEXAM = serializers.IntegerField(
        source="min_exam", required=False, allow_null=True
    )
    CrewList = serializers.CharField(
        source="crew_list", required=False, allow_blank=True
    )
    DateBASE = serializers.DateField(source="date_base", required=False)
    FuelUsed = serializers.IntegerField(
        source="fuel_used", required=False, allow_null=True
    )
    HobbsOut = serializers.IntegerField(
        source="hobbs_out", required=False, allow_null=True
    )
    LdgNight = serializers.IntegerField(
        source="ldg_night", required=False, allow_null=True
    )
    NextPage = serializers.BooleanField(source="next_page", required=False)
    TagDelay = serializers.CharField(
        source="tag_delay", required=False, allow_blank=True
    )
    Training = serializers.CharField(
        source="training", required=False, allow_blank=True
    )
    UserBool = serializers.BooleanField(source="user_bool", required=False)
    UserText = serializers.CharField(
        source="user_text", required=False, allow_blank=True
    )
    minINSTR = serializers.IntegerField(
        source="min_instr", required=False, allow_null=True
    )
    minNIGHT = serializers.IntegerField(
        source="min_night", required=False, allow_null=True
    )
    minPICUS = serializers.IntegerField(
        source="min_picus", required=False, allow_null=True
    )
    minTOTAL = serializers.IntegerField(
        source="min_total", required=False, allow_null=True
    )
    ArrOffset = serializers.IntegerField(
        source="arr_offset", required=False, allow_null=True
    )
    DateLOCAL = serializers.DateField(source="date_local", required=False)
    DepOffset = serializers.IntegerField(
        source="dep_offset", required=False, allow_null=True
    )
    TagLaunch = serializers.CharField(
        source="tag_launch", required=False, allow_blank=True
    )
    TagLesson = serializers.CharField(
        source="tag_lesson", required=False, allow_blank=True
    )
    ToTimeUTC = serializers.IntegerField(
        source="to_time_utc", required=False, allow_null=True
    )
    ArrTimeUTC = serializers.IntegerField(
        source="arr_time_utc", required=False, allow_null=True
    )
    BaseOffset = serializers.IntegerField(
        source="base_offset", required=False, allow_null=True
    )
    DepTimeUTC = serializers.IntegerField(
        source="dep_time_utc", required=False, allow_null=True
    )
    LdgTimeUTC = serializers.IntegerField(
        source="ldg_time_utc", required=False, allow_null=True
    )
    FuelPlanned = serializers.IntegerField(
        source="fuel_planned", required=False, allow_null=True
    )
    NextSummary = serializers.BooleanField(source="next_summary", required=False)
    TagApproach = serializers.CharField(
        source="tag_approach", required=False, allow_blank=True
    )
    AircraftCode = serializers.CharField(required=False, allow_blank=True)
    ArrTimeSCHED = serializers.IntegerField(
        source="arr_time_sched", required=False, allow_null=True
    )
    DepTimeSCHED = serializers.IntegerField(
        source="dep_time_sched", required=False, allow_null=True
    )
    FlightNumber = serializers.CharField(
        source="flight_number", required=False, allow_blank=True
    )
    FlightSearch = serializers.CharField(
        source="flight_search", required=False, allow_blank=True
    )
    Record_Modified = serializers.IntegerField(
        source="record_modified", required=False, allow_null=True
    )

    class Meta(BaseFlightSerializer.Meta):
        fields = [
            "FlightCode",
            "PF",
            "Pax",
            "Fuel",
            "DeIce",
            "Route",
            "ToDay",
            "minU1",
            "minU2",
            "minU3",
            "minU4",
            "minXC",
            "ArrRwy",
            "DepRwy",
            "LdgDay",
            "LiftSW",
            "P1Code",
            "P2Code",
            "P3Code",
            "P4Code",
            "Report",
            "TagOps",
            "ToEdit",
            "minAIR",
            "minCOP",
            "minIFR",
            "minIMT",
            "minPIC",
            "minREL",
            "minSFR",
            "ArrCode",
            "DateUTC",
            "DepCode",
            "HobbsIn",
            "Holding",
            "Pairing",
            "Remarks",
            "SignBox",
            "ToNight",
            "UserNum",
            "minDUAL",
            "minEXAM",
            "CrewList",
            "DateBASE",
            "FuelUsed",
            "HobbsOut",
            "LdgNight",
            "NextPage",
            "TagDelay",
            "Training",
            "UserBool",
            "UserText",
            "minINSTR",
            "minNIGHT",
            "minPICUS",
            "minTOTAL",
            "ArrOffset",
            "DateLOCAL",
            "DepOffset",
            "TagLaunch",
            "TagLesson",
            "ToTimeUTC",
            "ArrTimeUTC",
            "BaseOffset",
            "DepTimeUTC",
            "LdgTimeUTC",
            "FuelPlanned",
            "NextSummary",
            "TagApproach",
            "AircraftCode",
            "ArrTimeSCHED",
            "DepTimeSCHED",
            "FlightNumber",
            "FlightSearch",
            "Record_Modified",
        ]

    def create(self, validated_data):
        # Resolve pilot codes to Pilot instances
        for pilot_field, code_field in [
            ("p1", "P1Code"),
            ("p2", "P2Code"),
            ("p3", "P3Code"),
            ("p4", "P4Code"),
        ]:
            code = validated_data.pop(code_field, None)
            if code and code.strip():
                try:
                    validated_data[pilot_field] = Pilot.objects.get(guid=code)
                except Pilot.DoesNotExist:
                    validated_data[pilot_field] = None
            else:
                validated_data[pilot_field] = None

        # Resolve airfield codes to Airfield instances
        for airfield_field, code_field in [
            ("arr_airfield", "ArrCode"),
            ("dep_airfield", "DepCode"),
        ]:
            code = validated_data.pop(code_field, None)
            if code and code.strip():
                try:
                    validated_data[airfield_field] = Airfield.objects.get(guid=code)
                except Airfield.DoesNotExist:
                    validated_data[airfield_field] = None
            else:
                validated_data[airfield_field] = None

        # Resolve aircraft code to Aircraft instance
        aircraft_code = validated_data.pop("AircraftCode", None)
        if aircraft_code and aircraft_code.strip():
            try:
                validated_data["aircraft"] = Aircraft.objects.get(guid=aircraft_code)
            except Aircraft.DoesNotExist:
                validated_data["aircraft"] = None
        else:
            validated_data["aircraft"] = None

        return super().create(validated_data)


class LogbookRecordSerializer(serializers.Serializer):
    table = serializers.CharField()
    meta = serializers.DictField()
    guid = serializers.CharField(required=False)
    platform = serializers.IntegerField(required=False)
    _modified = serializers.IntegerField(required=False)
