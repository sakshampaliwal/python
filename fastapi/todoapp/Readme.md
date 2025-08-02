# FastAPI To-Do Application

This is a simple **To-Do List API** built using [FastAPI](https://fastapi.tiangolo.com/) — a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.

The API supports full **CRUD** (Create, Read, Update, Delete) operations on to-do items stored in memory. Note that the data is not persisted and will be lost upon server restart.

---

## Table of Contents

1. [Tech Stack](#tech-stack)
2. [Folder Structure](#folder-structure)
3. [Getting Started](#getting-started)

   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
   * [Running the Application](#running-the-application)
4. [API Endpoints](#api-endpoints)
5. [Example Request Body](#example-request-body)
6. [Code Architecture & MVC Pattern](#code-architecture--mvc-pattern)
7. [Why Use Pydantic for Validation](#why-use-pydantic-for-validation)
8. [Import Fix for Folder Structure](#import-fix-for-folder-structure)
9. [Notes](#notes)

---

## Tech Stack

| Technology       | Description                                                           |
| ---------------- | --------------------------------------------------------------------- |
| **FastAPI**      | Web framework for building high-performance APIs                      |
| **Pydantic**     | Data validation and settings management using Python type annotations |
| **Uvicorn**      | ASGI server for running FastAPI applications                          |
| **Python 3.12+** | Programming language used for development                             |

---

## Folder Structure

```
📦 fastapi
 ┣ 📂app
 ┃ ┣ 📜main.py         # FastAPI routes and core logic
 ┃ ┗ 📜models.py       # Pydantic model for Todo items
 ┣ 📜.env              # (Optional) Environment variables
 ┣ 📜.gitignore        # Files and folders ignored by Git
 ┣ 📜README.md         # Project documentation
 ┣ 📜Requirements.txt  # Python dependencies

```

---

## Getting Started

### Prerequisites

* Python 3.12 or later
* `pip` (Python package installer)
* (Optional) `virtualenv` for creating isolated environments

### Installation

Install the required dependencies:

```bash
pip install -r Requirements.txt
```

Contents of `Requirements.txt`:

```
fastapi
uvicorn
```

### Running the Application

Start the FastAPI application with the following command:

```bash
uvicorn app.main:app --reload
```

Explanation:

* `app.main` refers to the `main.py` file inside the `app/` directory.
* `:app` refers to the `FastAPI()` instance named `app` inside that file.

Once running, the application is available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints

| Method | Endpoint           | Description                     |
| ------ | ------------------ | ------------------------------- |
| GET    | `/`                | Returns a welcome message       |
| POST   | `/todos/`          | Create a new to-do item         |
| GET    | `/todos/`          | Retrieve all to-do items        |
| GET    | `/todos/{todo_id}` | Retrieve a specific to-do by ID |
| PUT    | `/todos/{todo_id}` | Update an existing to-do by ID  |
| DELETE | `/todos/{todo_id}` | Delete a to-do item by ID       |

---

## Example Request Body

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Study FastAPI framework and build a project",
  "completed": false
}
```

---

## Code Architecture & MVC Pattern

FastAPI apps often follow a pattern similar to **MVC (Model-View-Controller)**, although it's not enforced:

* **Models** (`models.py`): Define what your data looks like. In this app, it defines the structure of a Todo item using Pydantic.
* **Views/Routes** (`main.py`): Handle API endpoints and request/response logic.
* **Database (not implemented here)**: Would normally live in a `db/` or `repository/` folder to manage persistence.

While this example does not include a full database layer or controller abstraction, the structure is kept modular and clean to allow future extension.

---

## Why Use Pydantic for Validation

You could manually validate data like this:

```python
if not isinstance(data["id"], int):
    raise Exception("id must be int")
```

However, this approach is:

* Repetitive and error-prone
* Difficult to scale as models become more complex
* Lacks auto-generated documentation and error messaging

**Pydantic** provides a better way:

```python
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
```

Benefits of using Pydantic with FastAPI:

* Automatic type validation
* Standardized, detailed error messages
* Automatic generation of interactive documentation
* Clean, maintainable code

**Conclusion**: Pydantic simplifies the validation process, improves reliability, and enhances API documentation — all with minimal boilerplate.

---

## Import Fix for Folder Structure

Your `main.py` file is inside the `app/` directory. When you write:

```python
from models import Todo
```

Python will raise an error, as it's trying to find `models.py` in the same directory. The correct import should be:

```python
from app.models import Todo
```

This reflects the proper module path based on your folder layout.

---

## Note:

* This project stores data in memory (`todo_list = []`). All data will be lost when the server is restarted.
* FastAPI automatically provides interactive API documentation:

  * Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  * ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---
