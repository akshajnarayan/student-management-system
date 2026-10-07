# Student Management System

A terminal-based student management system built with Python.

## Features

* Interactive menu-driven interface
* Add student records
* View all student records
* Search students by student ID
* Update student details
* Remove student records
* Persistent data storage using JSON
* Modular program structure
* Basic terminal animations

## Project Structure

```text
student-management-system/
├── main.py
├── ui.py
├── core.py
├── storage.py
├── animations.py
├── README.md
└── data/
    └── students.json
```

### Modules

* **`main.py`** — Program entry point, main menu, and high-level program flow.
* **`ui.py`** — Handles user interaction, input collection, validation, and displaying information.
* **`core.py`** — Contains the operations that manipulate student data.
* **`storage.py`** — Handles loading and storing student records using JSON.
* **`animations.py`** — Provides basic terminal animations, including spinners, loading indicators, progress bars, and changing status messages.
* **`data/students.json`** — Stores student records between program runs.

## Data Storage

Student records are stored in `data/students.json`, allowing data to persist between program runs.

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```
