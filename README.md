# Django-Practice
Learning Django by implementing a simple RESTful api and a data ingestion server
- [📘 Progress and Learning Notes](./progress-tracker.md)
# 🐍 FastAPI Best Practices — Data Ingestion Pipeline

This project is a **FastAPI server** built to demonstrate **best practices** in designing clean, testable, and maintainable Python backends — especially focused on building **data ingestion pipelines**.

It’s not tied to any specific product or frontend. The goal is to showcase:
- A robust backend using **FastAPI**
- Integration with a **PostgreSQL** database
- Use of a **third-party API** to retrieve data
- A simple **data ingestion pipeline**
- Complete **CRUD operations** on the ingested data
- **Test coverage** for both the ingestion logic and API endpoints

---

## 🚀 Tech Stack

- **FastAPI**: High-performance async Python web framework
- **PostgreSQL**: Relational database
- **SQLAlchemy / asyncpg / psycopg2**: (your choice) for database interaction
- **Pydantic**: Data validation and parsing
- **httpx / requests**: For calling external APIs
- **pytest**: Testing framework
- **Docker** (optional): For containerization and environment setup

---

## 📦 Features

- Best practices from [Kraken Flex's Python guidelines](https://github.com/octoenergy/public-conventions) applied throughout
- Clean API structure (no framework opinions on directory structure)
- Third-party API integration
- Custom data ingestion and transformation logic
- Full CRUD routes
- Unit and integration test coverage

---

## 🌐 Example Third-Party APIs (Free & Public)

You can experiment with any of the following APIs:

| API | Description | Endpoint |
|-----|-------------|----------|
| [Open-Meteo](https://open-meteo.com/en/docs) | Free weather forecast API (no key required) | `https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m` |
| [Public APIs](https://github.com/public-apis/public-apis) | A curated list of free APIs | *(list of many)* |
| [ExchangeRate Host](https://exchangerate.host) | Free currency exchange API | `https://api.exchangerate.host/latest?base=USD` |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Mock JSON API for testing | `https://jsonplaceholder.typicode.com/posts` |

---

## 📁 Project Structure

> This project follows Kraken Flex guidelines.  
> **No opinionated directory structure is included here.**

---

## ✅ Running the App

```bash
# Install dependencies
poetry install  # or pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
