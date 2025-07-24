import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_logbook_import_with_errors():
    """Test logbook import with invalid data"""
    client = APIClient()
    url = reverse('logbook-import-logbook')
    payload = [
        {
            "table": "aircraft",
            "guid": "invalid-aircraft",
            "meta": {
                "AircraftCode": "invalid-aircraft",
                # Missing required fields Class and Record_Modified
                "Make": "Invalid Aircraft",
            }
        },
        {
            "table": "unknown_table",
            "guid": "some-guid",
            "meta": {"field": "value"}
        }
    ]
    
    response = client.post(url, payload, format='json')
    assert response.status_code == 201  # API still returns 201 even with errors
    data = response.json()
    assert data['imported'] == 0
    assert len(data['errors']) == 2
    assert 'Class' in str(data['errors'][0]['error'])
    assert 'unknown_table' in data['errors'][1]['error']
