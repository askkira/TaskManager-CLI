import json
from datetime import datetime

FILE_NAME = "tasks.json"

# ---------------------- Storage ----------------------

def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

# ---------------------- Output Helpers ----------------------

def print_msg(msg=""):
    print(f"\n{msg}\n")

def sort_tasks_by_priority(tasks):
    priority_order = {"High": 3, "Medium": 2, "Low": 1}
    tasks.sort(key=lambda task: priority_order.get(task.get("priority", "Medium"), 2), reverse=True)

def print_tasks(tasks):
    if not tasks:
        print_msg("The task list is empty!")
        return
    sort_tasks_by_priority(tasks)
    print_msg("Tasks list:")
    for idx, task in enumerate(tasks, 1):
        status = "[x]" if task["done"] else "[ ]"
        priority = task.get("priority", "Medium")
        deadline = task.get("deadline", "No deadline")
        print(f"{status} {idx}. {task['title']} (Priority: {priority}, Deadline: {deadline})\n")

# ---------------------- Input Helpers ----------------------

def choose_priority():
    while True:
        print_msg("Select priority: 1-High, 2-Medium, 3-Low (Enter for Medium)")
        choice = input("Enter number (1-3) or leave blank: ").strip()
        if choice == "":
            return "Medium"
        if choice in ("1","2","3"):
            return {"1":"High","2":"Medium","3":"Low"}[choice]
        print_msg("Invalid choice! Please enter (1-3) or press Enter for Medium.")

def choose_deadline():
    while True:
        deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ").strip()
        if deadline == "":
            return "No deadline"
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            return deadline
        except ValueError:
            print_msg("Invalid date format! Please enter in YYYY-MM-DD format.")

def require_tasks(tasks):
    if not tasks:
        print_msg("The task list is empty!")
        return False
    return True

def ask_task_number(tasks, prompt):
    if not require_tasks(tasks):
        return None
    while True:
        print_tasks(tasks)
        number = input(f"{prompt} (Enter to cancel): ").strip()
        if number == "":
            return None
        try:
            n = int(number)
            if 1 <= n <= len(tasks):
                return n - 1
            else:
                print_msg("Invalid task number! Try again.")
        except ValueError:
            print_msg("Please enter a valid number!")

# ---------------------- Task Operations ----------------------

def add_task(tasks):
    while True:
        title = input("Enter task name (Enter to cancel): ").strip()
        if title == "":
            return
        if any(task["title"].lower() == title.lower() for task in tasks):
            print_msg(f"Task '{title}' already exists!")
            continue
        priority = choose_priority()
        deadline = choose_deadline()
        tasks.append({
            "title": title,
            "done": False,
            "priority": priority,
            "deadline": deadline
        })
        save_tasks(tasks)
        print_msg(f"Task '{title}' added!")
        print_tasks(tasks)
        break

def delete_task(tasks):
    if not require_tasks(tasks):
        return
    while True:
        idx = ask_task_number(tasks, "Enter task number to delete")
        if idx is None:
            return
        task = tasks[idx]
        confirm = input(f"Are you sure you want to delete '{task['title']}'? (y/n): ").strip().lower()
        if confirm == "y":
            tasks.pop(idx)
            save_tasks(tasks)
            print_msg(f"Task '{task['title']}' deleted!")
        else:
            print_msg("Deletion cancelled!")
        if not tasks:
            print_msg("No more tasks to delete.")
            return

def complete_task(tasks):
    idx = ask_task_number(tasks, "Enter task number to complete")
    if idx is None:
        return
    task = tasks[idx]
    if task["done"]:
        print_msg(f"Task '{task['title']}' is already completed!")
        return
    task["done"] = True
    save_tasks(tasks)
    print_msg(f"Task '{task['title']}' marked as completed!")

def revert_task(tasks):
    idx = ask_task_number(tasks, "Enter task number to revert to Pending")
    if idx is None:
        return
    task = tasks[idx]
    if not task["done"]:
        print_msg(f"Task '{task['title']}' is already Pending!")
        return
    task["done"] = False
    save_tasks(tasks)
    print_msg(f"Task '{task['title']}' reverted to Pending!")

def edit_task(tasks):
    idx = ask_task_number(tasks, "Enter task number to edit")
    if idx is None:
        return
    task = tasks[idx]
    new_title = input("Enter new task text (leave blank to keep current): ").strip()
    if new_title:
        if any(t["title"].lower() == new_title.lower() for t in tasks if t != task):
            print_msg("Task with this name already exists!")
            return
        task["title"] = new_title
    print_msg(f"Current priority: {task['priority']}")
    task['priority'] = choose_priority()
    print_msg(f"Current deadline: {task['deadline']}")
    task['deadline'] = choose_deadline()
    save_tasks(tasks)
    print_msg("Task edited!")

# ---------------------- Main ----------------------

def main():
    tasks = load_tasks()
    while True:
        print_msg("--- Task Manager ---")
        print("1: Show tasks")
        print("2: Add task")
        print("3: Delete task")
        print("4: Complete task")
        print("5: Revert task")
        print("6: Edit task")
        print("7: Exit")
        choice = input("Select an action: ").strip()
        if choice == "1":
            print_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            revert_task(tasks)
        elif choice == "6":
            edit_task(tasks)
        elif choice == "7":
            print_msg("Exiting Task Manager...")
            break
        else:
            print_msg("Invalid choice! Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()