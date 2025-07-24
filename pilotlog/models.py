import uuid
from django.db import models


class BaseModel(models.Model):
    # user_id = models.IntegerField()
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    platform = models.IntegerField(null=True, blank=True)
    _modified = models.IntegerField(null=True, blank=True)  # timestamp?

    class Meta:
        abstract = True


class Aircraft(BaseModel):
    fin = models.CharField(max_length=20, blank=True)
    sea = models.BooleanField(default=False)
    tmg = models.BooleanField(default=False)
    efis = models.BooleanField(default=False)
    fnpt = models.IntegerField(default=0)
    make = models.CharField(max_length=100)
    run2 = models.BooleanField(default=False)
    aircraft_class = models.IntegerField()  # 'Class' is a reserved word
    model = models.CharField(max_length=100)
    power = models.IntegerField(default=1)
    seats = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    kg5700 = models.BooleanField(default=False)
    rating = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100)
    complex = models.BooleanField(default=False)
    cond_log = models.IntegerField()
    fav_list = models.BooleanField(default=False)
    category = models.IntegerField()
    high_perf = models.BooleanField(default=False)
    sub_model = models.CharField(max_length=100, blank=True)
    aerobatic = models.BooleanField(default=False)
    ref_search = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    tailwheel = models.BooleanField(default=False)
    default_app = models.IntegerField(default=0)
    default_log = models.IntegerField(default=2)
    default_ops = models.IntegerField(default=0)
    device_code = models.IntegerField(default=1)
    default_launch = models.IntegerField(default=0)
    record_modified = models.IntegerField()

    @property
    def aircraft_code(self):
        return self.guid


class Airfield(BaseModel):
    af_cat = models.IntegerField()
    af_iata = models.CharField(max_length=10)
    af_icao = models.CharField(max_length=10)
    af_name = models.CharField(max_length=100)
    tz_code = models.IntegerField()
    latitude = models.IntegerField()
    show_list = models.BooleanField(default=False)
    af_country = models.IntegerField()
    longitude = models.IntegerField()
    notes_user = models.CharField(max_length=255, blank=True)
    region_user = models.IntegerField(default=0)
    elevation_ft = models.IntegerField(default=0)
    record_modified = models.IntegerField()

    @property
    def af_code(self):
        return self.guid


class Flight(BaseModel):
    pf = models.BooleanField(default=False)
    pax = models.IntegerField(default=0)
    fuel = models.IntegerField(default=0)
    deice = models.BooleanField(default=False)
    route = models.CharField(max_length=255, blank=True)
    to_day = models.IntegerField(default=0)
    min_u1 = models.IntegerField(default=0)
    min_u2 = models.IntegerField(default=0)
    min_u3 = models.IntegerField(default=0)
    min_u4 = models.IntegerField(default=0)
    min_xc = models.IntegerField(default=0)
    arr_rwy = models.CharField(max_length=20, blank=True)
    dep_rwy = models.CharField(max_length=20, blank=True)
    ldg_day = models.IntegerField(default=0)
    lift_sw = models.IntegerField(default=0)
    p1 = models.ForeignKey(
        "Pilot",
        to_field="guid",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="as_p1",
    )
    p2 = models.ForeignKey(
        "Pilot",
        to_field="guid",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="as_p2",
    )
    p3 = models.ForeignKey(
        "Pilot",
        to_field="guid",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="as_p3",
    )
    p4 = models.ForeignKey(
        "Pilot",
        to_field="guid",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="as_p4",
    )
    report = models.TextField(blank=True)
    tag_ops = models.CharField(max_length=100, blank=True)
    to_edit = models.BooleanField(default=False)
    min_air = models.IntegerField(default=0)
    min_cop = models.IntegerField(default=0)
    min_ifr = models.IntegerField(default=0)
    min_imt = models.IntegerField(default=0)
    min_pic = models.IntegerField(default=0)
    min_rel = models.IntegerField(default=0)
    min_sfr = models.IntegerField(default=0)
    arr_airfield = models.ForeignKey(
        "Airfield",
        to_field="guid",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="arrivals",
    )
    date_utc = models.DateField(null=True, blank=True)
    dep_airfield = models.ForeignKey(
        "Airfield",
        to_field="guid",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="departures",
    )
    hobbs_in = models.IntegerField(default=0)
    holding = models.IntegerField(default=0)
    pairing = models.CharField(max_length=100, blank=True)
    remarks = models.TextField(blank=True)
    sign_box = models.IntegerField(default=0)
    to_night = models.IntegerField(default=0)
    user_num = models.IntegerField(default=0)
    min_dual = models.IntegerField(default=0)
    min_exam = models.IntegerField(default=0)
    crew_list = models.CharField(max_length=255, blank=True)
    date_base = models.DateField(null=True, blank=True)
    fuel_used = models.IntegerField(default=0)
    hobbs_out = models.IntegerField(default=0)
    ldg_night = models.IntegerField(default=0)
    next_page = models.BooleanField(default=False)
    tag_delay = models.CharField(max_length=100, blank=True)
    training = models.CharField(max_length=100, blank=True)
    user_bool = models.BooleanField(default=False)
    user_text = models.CharField(max_length=255, blank=True)
    min_instr = models.IntegerField(default=0)
    min_night = models.IntegerField(default=0)
    min_picus = models.IntegerField(default=0)
    min_total = models.IntegerField(default=0)
    arr_offset = models.IntegerField(default=0)
    date_local = models.DateField(null=True, blank=True)
    dep_offset = models.IntegerField(default=0)
    tag_launch = models.CharField(max_length=100, blank=True)
    tag_lesson = models.CharField(max_length=100, blank=True)
    to_time_utc = models.IntegerField(default=0)
    arr_time_utc = models.IntegerField(default=0)
    base_offset = models.IntegerField(default=0)
    dep_time_utc = models.IntegerField(default=0)
    ldg_time_utc = models.IntegerField(default=0)
    fuel_planned = models.IntegerField(default=0)
    next_summary = models.BooleanField(default=False)
    tag_approach = models.CharField(max_length=100, blank=True)
    aircraft = models.ForeignKey(
        "Aircraft",
        to_field="guid",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="flights",
    )
    arr_time_sched = models.IntegerField(default=0)
    dep_time_sched = models.IntegerField(default=0)
    flight_number = models.CharField(max_length=20, blank=True)
    flight_search = models.CharField(max_length=100)
    record_modified = models.IntegerField(default=0)

    @property
    def flight_code(self):
        return self.guid


class Pilot(BaseModel):
    notes = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    company = models.CharField(max_length=100)
    fav_list = models.BooleanField(default=False)
    user_api = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    pilot_ref = models.CharField(max_length=20)
    pilot_name = models.CharField(max_length=100)
    pilot_email = models.EmailField(blank=True)
    pilot_phone = models.CharField(max_length=20, blank=True)
    certificate = models.CharField(max_length=100, blank=True)
    phone_search = models.CharField(max_length=20, blank=True)
    pilot_search = models.CharField(max_length=100)
    roster_alias = models.CharField(max_length=100, blank=True)
    record_modified = models.IntegerField()

    @property
    def pilot_code(self):
        return self.guid


class Qualification(BaseModel):
    ref_extra = models.IntegerField(default=0)
    ref_model = models.CharField(max_length=100)
    validity = models.IntegerField(default=0)
    date_valid = models.DateField(null=True, blank=True)
    qtype_code = models.IntegerField()
    date_issued = models.DateField(null=True, blank=True)
    minimum_qty = models.IntegerField(default=0)
    notify_days = models.IntegerField(default=0)
    ref_airfield = models.ForeignKey(
        "Airfield",
        to_field="guid",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="qualifications",
    )
    minimum_period = models.IntegerField(default=0)
    notify_comment = models.CharField(max_length=255, blank=True)
    record_modified = models.IntegerField()

    @property
    def q_code(self):
        return self.guid


# imagepic
# LimitRules
# SettingConfig
# myQuery
# myQueryBuild
