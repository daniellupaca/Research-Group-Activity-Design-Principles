# Software Design Principles: KISS and YAGNI in Python

This repository demonstrates how to apply two important software design principles — **KISS (Keep It Simple, Stupid)** and **YAGNI (You Aren’t Gonna Need It)** — using a simple task management example written in Python.

## Overview

The Python script allows you to:

- Add tasks
- List tasks
- Mark tasks as completed

## Code Example

```python
tasks = []

def add_task(description):
    tasks.append({"description": description, "done": False})

def list_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['description']}")

def complete_task(index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
```

## Usage

```bash
python tasks.py
```

## Principles Demonstrated

- **KISS**: Code is clean and simple.
- **YAGNI**: Only includes features required now — no unnecessary abstraction or layers.

---

## GitHub Actions Automation

This project includes a GitHub Action to automatically check Python code formatting using `flake8`.

##  File structure

```
.
├── tasks.py
├── .github
│   └── workflows
│       └── lint.yml
└── README.md
```

---

## Video Demo

Watch the video that explains the code and principles:

🔗 https://youtube.com/your-video-link

---

## 📄 License

MIT