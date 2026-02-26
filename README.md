# CompanyAnalysis
Analysing Companies for future sales oppurtunities.

# CompanyAnalysis Backend

A FastAPI-based backend service for company analysis.
## Backend
### Prerequisites

- Python 3.12+
- pip
- uv

### Installation

```bash
uv init
```

### Running the Server

Start the development server with uvicorn:

```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
