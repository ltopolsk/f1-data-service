# F1 Data Aggregation Service
Production-grade backend service providing Formula 1 data, built with modern Python practices.

This project demonstrates a Hexagonal Architecture (Ports and Adapters) approach to building scalable backend systems. It integrates with the Jolpica-F1 public API to fetch, process, and serve F1 race data while maintaining strict separation of concerns.

# Key Features

- Clean Architecture: Strict separation between Domain, Application (Service), and Infrastructure layers.
- Async First: Fully asynchronous I/O using httpx and FastAPI.
- Robust Error Handling: Custom domain exceptions and defensive programming patterns.
- Type Safety: 100% type-hinted codebase utilizing Pydantic v2 for data validation.
- Modern Tooling: Dependency management and virtual environments handled by uv.

# Tech stack
| Category        | Technology   |
|-----------------|--------------|
| Language        | Python 3.12+ |
| Web Framework   | FastAPI      |
| Package Manager | uv           | 
| HTTP Client     | httpx        |
| Data Validation | Pydantic v2  |
| Testing         | pytest       |
| Data Source     | Jolpica-F1   |

# Project Structure
The project follows a modular structure to ensure maintanability:
```
    app/
    ├── api/             # Entry points (FastAPI routers) - Presentation Layer
    ├── core/            # App configuration, logging, and base exceptions
    ├── domain/          # Pure business logic and data models (No external deps)
    ├── infrastructure/  # External adapters (Jolpica Client, Database, Cache)
    └── services/        # Orchestration logic (Use Cases)
    tests/               # Unit and Integration tests
```

# Getting Started
This project uses uv for dependency management.

## Prerequisites
- Python 3.12 or higher
- `uv` installed (`pip install uv` or via brew/curl)

## 1. Clone and setup

```bash
git clone https://github.com/ltopolsk/f1-data-service.git
cd f1-data-service

# Create virtualenv and sync dependencies
uv sync
```

## 2. Run Tests
To verify the logic and external integration:
```bash
# Run all tests
uv run pytest

# Run specific integration check
uv run python test/main_test.py
```

## 3. Run Application (Local Development)

Start the hot-reloading development server:
```bash
uv run uvicorn app.main:app --reload
```
API will be available at http://localhost:8000 (Docs at /docs)

# Run with Docker
To build and run the containerized application:
```bash
docker compose up --build
```
