import pandas as pd
import logging
from .models import Aircraft, Flight
from .serializers.export_serializers import (
    AircraftExportSerializer,
    FlightExportSerializer,
)

logger = logging.getLogger(__name__)

TEMPLATE_COLUMNS_AIRCRAFT = [
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

STATIC_HEADER_ROWS_AIRCRAFT = [
    "ForeFlight Logbook Import" + "," * 60,
    "," * 60,
    "Aircraft Table" + "," * 60,
    "Text,Text,Text,YYYY,Text,Text,Text,Text,Text,Text,Boolean,Boolean,Boolean,Boolean"
    + "," * 60,
    "AircraftID,EquipmentType,TypeCode,Year,Make,Model,Category,Class,GearType,EngineType,Complex,HighPerformance,Pressurized,TAA"
    + "," * 60,
    "," * 60,
]

TEMPLATE_COLUMNS_FLIGHT = [
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

STATIC_HEADER_ROWS_FLIGHT = [
    "Flights Table" + "," * 60,
    "Date,Text,Text,Text,Text,hhmm,hhmm,hhmm,hhmm,hhmm,hhmm,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Number,Decimal,Number,Number,Number,Number,Number,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Number,Packed Detail,Packed Detail,Packed Detail,Packed Detail,Packed Detail,Packed Detail,Decimal,Decimal,Decimal,Decimal,Text,Text,Packed Detail,Packed Detail,Packed Detail,Packed Detail,Packed Detail,Packed Detail,Boolean,Boolean,Boolean,Boolean,Boolean,Text,Decimal,Decimal,Number,Date,DateTime,Boolean,Text",
    "Date,AircraftID,From,To,Route,TimeOut,TimeOff,TimeOn,TimeIn,OnDuty,OffDuty,TotalTime,PIC,SIC,Night,Solo,CrossCountry,NVG,NVGOps,Distance,DayTakeoffs,DayLandingsFullStop,NightTakeoffs,NightLandingsFullStop,AllLandings,ActualInstrument,SimulatedInstrument,HobbsStart,HobbsEnd,TachStart,TachEnd,Holds,Approach1,Approach2,Approach3,Approach4,Approach5,Approach6,DualGiven,DualReceived,SimulatedFlight,GroundTraining,InstructorName,InstructorComments,Person1,Person2,Person3,Person4,Person5,Person6,FlightReview,Checkride,IPC,NVGProficiency,FAA6158,TextCustomFieldName,NumericCustomFieldName,HoursCustomFieldName,CounterCustomFieldName,DateCustomFieldName,DateTimeCustomFieldName,ToggleCustomFieldName,PilotComments",
    "," * 60,
]


def export_aircraft_to_csv(file_obj):
    logger.info("Exporting aircraft data to CSV...")
    for row in STATIC_HEADER_ROWS_AIRCRAFT:
        file_obj.write(row + "\n")
    qs = Aircraft.objects.all()
    data = [AircraftExportSerializer(obj).data for obj in qs]
    df = pd.DataFrame(data)
    df = df.reindex(columns=TEMPLATE_COLUMNS_AIRCRAFT, fill_value="")
    df.to_csv(file_obj, index=False, header=False)
    logger.info("Aircraft data export complete.")


def export_flights_to_csv(file_obj):
    logger.info("Exporting flight data to CSV...")
    for row in STATIC_HEADER_ROWS_FLIGHT:
        file_obj.write(row + "\n")
    qs = Flight.objects.all()
    data = [FlightExportSerializer(obj).data for obj in qs]
    df = pd.DataFrame(data)
    df = df.reindex(columns=TEMPLATE_COLUMNS_FLIGHT, fill_value="")
    df.to_csv(file_obj, index=False, header=False)
    logger.info("Flight data export complete.")
