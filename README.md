# Student Management System

A terminal-based student management system built with Python.

## Features

* Interactive menu-driven interface
* Add student records
* View all student records
* Search students by roll number
* Update student details
* Remove student records
* Persistent data storage using JSON
* Modular program structure

## Project Structure

```text
student-management-system/
├── main.py
├── ui.py
├── core.py
├── storage.py
├── students.json
└── README.md
```

### Modules

* **`main.py`** — Program entry point, main menu, and high-level program flow.
* **`ui.py`** — Handles user interaction, input collection, validation, and displaying information.
* **`core.py`** — Contains the operations that manipulate student data.
* **`storage.py`** — Handles loading and storing student records using JSON.
* **`students.json`** — Stores student records between program runs.

## Data Storage

Student records are stored in `students.json`, allowing data to persist between program runs.

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```
