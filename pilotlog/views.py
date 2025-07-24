from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .serializers.import_serializers import (
    LogbookRecordSerializer,
)
from .export_csv import export_aircraft_to_csv, export_flights_to_csv
import io
import logging
from .importer import import_logbook_records

logger = logging.getLogger(__name__)


class LogbookViewSet(viewsets.ViewSet):
    SUPPORTED_TABLES = ["aircraft", "flight"]

    @action(detail=False, methods=["post"], url_path="import")
    def import_logbook(self, request):
        """
        Import logbook records for supported tables.
        """
        import_serializer = LogbookRecordSerializer(data=request.data, many=True)
        import_serializer.is_valid(raise_exception=True)
        records = import_serializer.validated_data

        results, errors = import_logbook_records(records)
        return Response(
            {"imported": len(results), "errors": errors, "results": results},
            status=status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["get"], url_path="export")
    def export_logbook(self, request):
        """
        Export logbook data as a CSV matching the ForeFlight template.
        """
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="logbook_export.csv"'
        buf = io.StringIO()
        logger.info("Exporting aircraft data to CSV...")
        export_aircraft_to_csv(buf)
        logger.info("Exporting flight data to CSV...")
        export_flights_to_csv(buf)
        response.write(buf.getvalue())
        buf.close()
        logger.info("Export completed.")
        return response
