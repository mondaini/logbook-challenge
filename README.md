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
fleek/
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
   cd fleek
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

### API Usage

#### Import Logbook Data

```bash
curl -X POST http://localhost:8000/api/logbook/import/ \
  -H "Content-Type: application/json" \
  -d @data/import/import-pilotlog_mcc.json
```

#### Export Logbook Data

```bash
curl -X GET http://localhost:8000/api/logbook/export/ \
  -o logbook_export.csv
```

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

## Dependency Management

All dependencies are managed via `pyproject.toml` using [uv](https://github.com/astral-sh/uv). This is the recommended and supported workflow for this project.

- To add a new dependency:
  ```bash
  uv pip install <package>
  uv pip freeze > pyproject.toml  # Or use uv's sync/lock commands as needed
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
