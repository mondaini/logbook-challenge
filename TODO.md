# Project Checklist: pilotlog

## Importer
- [x] Implement reusable importer module for JSON data
- [x] Map PascalCase import keys to model fields using ModelSerializer
- [x] Validate and import Aircraft data
- [ ] Validate and import Flight data (ModelSerializer mapping)
- [ ] Add support for additional tables/entities as needed

## Django App & Models
- [x] Create Django app `pilotlog`
- [x] Design normalized, DRY models for Aircraft, Flight, etc.
- [x] Ensure models are future-proof and adaptable

## Exporter
- [ ] Implement reusable CSV exporter module
- [ ] Match export format to `export-logbook_template.csv`
- [ ] Integrate exporter with `export_logbook` endpoint

## Testing
- [x] Add unit tests for import serializers (valid, missing, wrong type, extra fields)
- [ ] Add integration tests for import endpoint with real data
- [ ] Add tests for CSV exporter output

## Documentation & Submission
- [ ] Write README with setup, usage, and extension instructions
- [ ] Push code to public GitHub repository
- [ ] Share direct link to the repository (not just org/user page) 