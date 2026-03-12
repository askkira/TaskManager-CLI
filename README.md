# Task Manager (Python)

A simple console-based Task Manager written in Python.

This program allows you to manage tasks directly from the terminal with priorities, deadlines, and completion status.

## Features

- Add tasks with title, priority (High / Medium / Low), and optional deadline.
- Delete tasks with confirmation.
- Mark tasks as completed.
- Revert completed tasks back to pending.
- Edit task title, priority, and deadline.
- Tasks automatically sorted by priority (High → Low).
- Input validation for numbers and dates.
- Tasks saved in `tasks.json`.

## Requirements

Python 3.x

## Installation

Clone the repository:

git clone <repository-url>

Enter the project folder:

cd <repository-folder>

Run the program:

python task_manager.py

## Menu

When running the program you will see:

--- Task Manager ---
1: Show tasks
2: Add task
3: Delete task
4: Complete task
5: Revert task
6: Edit task
7: Exit

Select an option by entering the corresponding number.

## Notes

- Only deleting a task requires confirmation.
- Task titles must be unique.
- Press Enter for optional values like priority or deadline.
- Tasks are stored locally in `tasks.json`.

## Example tasks.json

[
  {
    "title": "Buy groceries",
    "done": false,
    "priority": "High",
    "deadline": "2026-03-15"
  }
]