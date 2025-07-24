import logging
from .models import Aircraft, Flight
from .serializers.import_serializers import (
    AircraftImportSerializer,
    FlightImportSerializer,
)

logger = logging.getLogger(__name__)

ENTITY_MAP = {
    "aircraft": (AircraftImportSerializer, Aircraft),
    "flight": (FlightImportSerializer, Flight),
}
SUPPORTED_TABLES = ["aircraft", "flight"]


def import_logbook_records(records):
    """
    Import logbook records for supported tables.
    Args:
        records (list[dict]): List of logbook records (already validated by LogbookRecordSerializer)
    Returns:
        tuple: (results, errors)
    """
    results, errors = [], []
    for idx, record in enumerate(records):
        table = record.get("table", "").lower()
        meta = record.get("meta", {})
        entity = ENTITY_MAP.get(table)
        logger.debug(f"Processing record {idx}: table={table} meta={meta}")
        if table not in SUPPORTED_TABLES or not entity:
            logger.warning(f"Unknown table/entity: {record.get('table')}")
            errors.append(
                {
                    "index": idx,
                    "table": record.get("table"),
                    "error": f"Unknown table/entity: {record.get('table')}",
                }
            )
            continue

        serializer_class, model_class = entity
        meta_serializer = serializer_class(data=meta)
        if meta_serializer.is_valid():
            obj = meta_serializer.save(guid=record.get("guid"))
            logger.info(f"Imported {table} record with guid={obj.guid}")
            results.append(
                {
                    "index": idx,
                    "table": record.get("table"),
                    "guid": str(obj.guid),
                    "created": True,
                }
            )
        else:
            logger.error(
                f"Serializer errors for record {idx} table={table}: {meta_serializer.errors}"
            )
            errors.append(
                {
                    "index": idx,
                    "table": record.get("table"),
                    "error": meta_serializer.errors,
                }
            )
    logger.info(f"Import completed: {len(results)} imported, {len(errors)} errors.")
    return results, errors
