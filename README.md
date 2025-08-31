# ☕ Django Café Simulation — Learning Project

This project is a **Django practice server** where I simulate the flow of a real-life café.  
The purpose is to **learn Django deeply**, experiment with background workers, and practice applying **clean backend best practices** inspired by [Kraken Flex’s Python guidelines](https://github.com/octoenergy/public-conventions).

---

## 🎯 Goals

1. **Customer Orders (CRUD):**  
   Build a simple API to track when customers buy coffee (Create, Read, Update, Delete).  

2. **Barista Simulation (Celery):**  
   Use Celery workers to simulate baristas making coffee in the background, continuously processing incoming orders.  

3. **Snappy Real-time Communication (Redis):**  
   Integrate Redis to mimic the speed of human interaction — baristas picking up orders instantly, customers receiving updates quickly.  

4. **Robustness (Simulated Power Outages):**  
   Ensure the system can recover after containers go down, so orders and barista tasks continue seamlessly when services restart.  

---

## 🚀 Tech Stack

- **Django**: Web framework for API and core logic  
- **Celery**: Background task queue for barista workflows  
- **Redis**: Message broker for Celery and real-time communication  
- **PostgreSQL**: Relational database for storing durable state (orders, customers, receipts)  
- **Docker**: Containerization for reproducible development  
- **pytest**: Testing framework  

-> using uv as the package manager and decontainers as the dev environment.

---

## 📦 Features

- **CRUD API** for managing customers and orders  
- **Background task processing** using Celery workers (simulating baristas making coffee)  
- **Redis-powered queue** for fast, real-time order handoffs  
- **Durable persistence** with PostgreSQL for recovering from outages  
- **Resilience testing** by simulating power outages (bringing down containers and restoring them)  
- **Best practices** inspired by Kraken Flex’s Python coding guidelines:  
  - Clean and testable backend design  
  - Explicit and validated data models  
  - Clear separation between API, domain logic, and infrastructure  

---

## 📁 Project Structure

This project follows Kraken Flex conventions.  
> ⚠️ No opinionated Django app directory structure is forced here. Instead, clarity, maintainability, and testability are prioritized.  

---
