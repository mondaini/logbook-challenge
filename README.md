# Fleek - Pilot Logbook Management System

A Django-based pilot logbook management system designed to import data from ForeFlight and export to standardized CSV formats.

## Features

- **Data Import**: Import pilot logbook data from JSON format (ForeFlight compatible)
- **Data Export**: Export aircraft and flight data to CSV format matching ForeFlight templates
- **RESTful API**: Full REST API for data import/export operations
- **Comprehensive Testing**: Unit and integration tests for all components
- **Modern Python**: Built with Python 3.11+, Django 5.2+, and modern tooling

## Project Structure

```
/
├── logbook/              # Django project settings
├── pilotlog/             # Main Django app
│   ├── models.py         # Database models (Aircraft, Flight, Pilot, Airfield)
│   ├── serializers/      # DRF serializers for import/export
│   ├── views.py          # API views and endpoints
│   ├── importer.py       # Data import logic
│   ├── export_csv.py     # CSV export functionality
│   └── tests/            # Comprehensive test suite
├── data/                 # Sample data files
│   ├── import/           # Import data examples
│   └── export/           # Export template examples
└── manage.py             # Django management script
```

## Quick Start

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended for Python projects)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd logbook-challenge
   ```

2. **Install dependencies using uv**
   ```bash
   uv sync
   ```
   This will install all dependencies as specified in `pyproject.toml`.

   > **Note:** If you must use pip, you can install dependencies with:
   > ```bash
   > pip install -r <(uv pip compile pyproject.toml)
   > ```
   > But `uv` is the recommended and supported method.

3. **Run migrations**
   ```bash
   uv run python manage.py migrate
   ```

4. **Start the development server**
   ```bash
   uv run python manage.py runserver
   ```

## API Usage

### Import Logbook Data

#### Using `curl`

```bash
curl -X POST http://localhost:8000/api/logbook/import/ \
  -H "Content-Type: application/json" \
  --data-binary @data/import/import-pilotlog_mcc.json
```

#### Using Postman

1. Create a new **POST** request.
2. Set the URL to: `http://localhost:8000/api/logbook/import/`
3. Go to the **Body** tab, select **raw**, and choose **JSON** from the dropdown.
4. Paste the contents of your JSON file (e.g., from `data/import/import-pilotlog_mcc.json`).
5. Click **Send**.

#### Example JSON Payload

```json
[
  {
    "table": "aircraft",
    "guid": "12345678-1234-5678-9abc-123456789012",
    "meta": {
      "AircraftCode": "12345678-1234-5678-9abc-123456789012",
      "Make": "Cessna",
      "Model": "C172",
      "Class": 2,
      "Company": "Flight School",
      "CondLog": 100,
      "Category": 1,
      "RefSearch": "C172",
      "Reference": "N12345",
      "Record_Modified": 1234567890
    }
  }
]
```

### Export Logbook Data

#### Using `curl`

```bash
curl -X GET http://localhost:8000/api/logbook/export/ -o logbook_export.csv
```

#### Using Postman

1. Create a new **GET** request.
2. Set the URL to: `http://localhost:8000/api/logbook/export/`
3. Click **Send**.
4. In the response, click **Save Response** to download the CSV file.

### API Documentation (Swagger/OpenAPI)

You can access interactive API documentation (Swagger UI) if you are running the server locally:

- Open your browser and go to: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)

This provides a full, interactive interface to explore and test all available endpoints.

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=pilotlog

# Run specific test file
uv run pytest pilotlog/tests/test_serializers.py
```

### Code Quality

We use [ruff](https://docs.astral.sh/ruff/) for both formatting and linting. No other code quality or type checking tools are required.

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check .
```

### Database Management

```bash
# Create new migration
uv run python manage.py makemigrations

# Apply migrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser
```

## Data Models

### Aircraft
- Unique identifier (GUID)
- Aircraft details (make, model, class, power, seats)
- Operational metadata (complex, high performance, etc.)

### Flight
- Flight details (route, times, durations)
- Aircraft and pilot relationships
- Operational data (fuel, weather, etc.)

### Pilot
- Pilot information and credentials
- Company and reference data

### Airfield
- Airport information (ICAO/IATA codes)
- Geographic data (coordinates, timezone)

## API Endpoints

- `POST /api/logbook/import/` - Import logbook data
- `GET /api/logbook/export/` - Export logbook data as CSV

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built for the Fleek coding challenge
- Designed to be compatible with ForeFlight logbook data formats
- Uses modern Django and Python best practices
