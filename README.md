# Task Manager

A simple **CLI-based Task Manager** written in Python to keep track of tasks with status, priority, and deadlines.

---

## Features

- Add, edit, delete tasks
- Mark tasks as completed or revert to pending
- **Priority selection** via numbers:
  - 1 → High
  - 2 → Medium
  - 3 → Low
- **Deadline input** in `YYYY-MM-DD` format with input validation
- All tasks show **status, title, priority, and deadline**
- Safe input handling — prevents errors from letters or incorrect numbers

---

## How to Use

1. Run the program:

```bash
python task_manager.py

	2.	Menu options:

1: Show tasks
2: Add task
3: Delete task
4: Complete task
5: Revert task
6: Edit task
7: Exit

	3.	Adding a task:
	•	Enter task name
	•	Choose priority via number (1–3)
	•	Enter deadline in YYYY-MM-DD format or leave blank
	4.	Editing a task:
	•	Select the task number
	•	Change name (optional)
	•	Choose new priority (via number)
	•	Enter new deadline (or leave blank to keep current)
	5.	Completing or reverting a task:
	•	Select the task number
	•	Confirm action (y/n)
	•	Task list shows updated status immediately

⸻

Example

[ ] 1. Finish homework (Priority: High, Deadline: 2026-03-20)
[x] 2. Buy groceries (Priority: Medium, Deadline: No deadline)

	•	[ ] → Pending
	•	[x] → Done

⸻

Installation

No external libraries required (standard Python 3.x).

Run with:

python task_manager.py


⸻

Notes
	•	Priority defaults to Medium if invalid input is given.
	•	Deadline defaults to No deadline if left blank or invalid.
	•	After every action, the task list updates automatically showing all details.
	•	Designed to be user-friendly and error-proof.

⸻

License

This project is open-source and free to use.
