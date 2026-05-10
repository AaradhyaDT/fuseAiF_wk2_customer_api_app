# Customer API App
**Fuse AI Fellowship 2026 - Week 2**

A RESTful API application for managing customer data built with FastAPI and PostgreSQL.

## Overview

This is a customer management API that provides endpoints to create, read, and update customer records. The application demonstrates best practices for building scalable REST APIs with Python, including database integration, error handling, and logging.

## Tech Stack

- **Framework**: FastAPI 0.136.1
- **Server**: Uvicorn 0.46.0
- **ORM**: SQLAlchemy 2.0.49
- **Database**: PostgreSQL (via psycopg2)
- **Data Validation**: Pydantic 2.13.4
- **Python**: 3.12+

## Features

- ✅ Create new customers
- ✅ Retrieve customer list with pagination
- ✅ Get individual customer details
- ✅ Update customer information
- ✅ Health check endpoint
- ✅ Database logging and error handling
- ✅ Docker and Docker Compose support

## Project Structure

```
├── main.py              # FastAPI application entry point
├── app/
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic validation schemas
│   ├── database.py      # Database connection and session management
│   ├── config.py        # Configuration settings
│   ├── logger.py        # Logging configuration
│   └── seed.sql         # Database initialization script
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Multi-container orchestration
├── pyproject.toml       # Project metadata and dependencies
└── requirements.txt     # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL database
- Docker (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fuseAiF_wk2_customer_api_app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/customer_db
   ```

5. **Initialize the database**
   ```bash
   # Run seed.sql script on your PostgreSQL instance
   psql -U user -d customer_db -f app/seed.sql
   ```

### Running the Application

**Locally:**
```bash
uvicorn main:app --reload
```

**With Docker Compose:**
```bash
docker-compose up
```

The API will be available at `http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/` | Welcome message |
| GET | `/customers` | List all customers (paginated) |
| POST | `/customers` | Create a new customer |
| GET | `/customers/{customer_id}` | Get customer by ID |
| PUT | `/customers/{customer_id}` | Update customer information |

### Query Parameters

- **GET /customers**
  - `skip`: Number of records to skip (default: 0)
  - `limit`: Maximum records to return (default: 10)

## Usage Examples

**Get all customers:**
```bash
curl http://localhost:8000/customers
```

**Create a new customer:**
```bash
curl -X POST http://localhost:8000/customers \
  -H "Content-Type: application/json" \
  -d '{
    "customerNumber": 123,
    "name": "John Doe",
    "email": "john@example.com"
  }'
```

**Get a specific customer:**
```bash
curl http://localhost:8000/customers/123
```

## Interactive API Documentation

Once running, access the interactive API documentation at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Development

### Logging

The application uses a custom logger configured in `app/logger.py`. Logs are output to the console and help with debugging and monitoring.

### Database

Database models are defined in `app/models.py` and Pydantic schemas for validation are in `app/schemas.py`. The `app/database.py` file manages the database connection and session lifecycle.

## Docker

Build and run the application in a Docker container:

```bash
# Build the image
docker build -t customer-api .

# Run the container
docker run -p 8000:8000 --env DATABASE_URL=<your-db-url> customer-api
```

## License

See LICENSE file for details.

## Support

For issues or questions, please refer to the Fuse AI Fellowship 2026 documentation.
