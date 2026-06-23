# Ask The Network

`ask_the_network` is a Python project scaffold for building a small question-and-answer workflow over network-related data.

The codebase is currently in the setup phase: package layout exists, and implementation files are in place but intentionally empty.

## Project Status

- Stage: initial scaffold
- Business logic: not implemented yet
- Data layer: planned (module present)
- Domain models: planned (module present)
- Config management: planned (module present)

## Repository Layout

```text
ask_the_network/
  README.md
  src/
    __init__.py
    core/
      __init__.py
      settings.py
    data/
      MOCK_DATA.csv
    data_models/
      __init__.py
      models.py
    database/
      __init__.py
      db.py
```

## Intended Module Responsibilities

- `src/core/settings.py`
  - Central app configuration
  - Environment variables and runtime defaults

- `src/data_models/models.py`
  - Domain/data model definitions
  - Validation and serialization boundaries

- `src/database/db.py`
  - Database connection setup
  - Query/repository helpers

- `src/data/MOCK_DATA.csv`
  - Seed/mock dataset for local development and testing

## Suggested Development Flow

1. Define settings contract in `src/core/settings.py`.
2. Add core entities in `src/data_models/models.py`.
3. Implement DB/session access in `src/database/db.py`.
4. Load and validate `src/data/MOCK_DATA.csv` through the model layer.
5. Add an entrypoint (for example, `src/main.py`) once core modules are ready.

## Local Setup (Planned)

This repository already includes a virtual environment folder (`.venv`) in the workspace. If needed, recreate and activate your own environment, then install dependencies once they are added.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet, create it when the first dependencies are introduced.

## Next Milestones

- Add initial dependencies and lock strategy
- Implement first model + CSV ingestion pipeline
- Add unit tests for configuration, models, and database layer
- Add CLI or minimal API entrypoint for "ask the network" queries

## Contributing Notes

- Keep module boundaries clear (`core`, `data_models`, `database`).
- Prefer small, testable functions.
- Add tests alongside new behavior as features are implemented.
