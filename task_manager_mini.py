import json
from datetime import datetime

FILE_NAME = "tasks.json"

# ---------------------- Storage ----------------------

def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

# ---------------------- Helpers ----------------------

def require_tasks(tasks):
    if not tasks:
        print("The task list is empty!")
        return False
    return True

def choose_priority():
    print("Select priority: 1-High, 2-Medium, 3-Low")
    choice = input("Enter number (1-3): ").strip()
    return {"1":"High","2":"Medium","3":"Low"}.get(choice,"Medium")

def choose_deadline():
    while True:
        d = input("Enter deadline YYYY-MM-DD or leave blank: ").strip()
        if not d:
            return "No deadline"
        try:
            datetime.strptime(d,"%Y-%m-%d")
            return d
        except ValueError:
            print("Invalid format! Try again.")

# ---------------------- Task Operations ----------------------

def show_tasks(tasks):
    if not tasks:
        print("Task list empty!")
        return
    for idx, task in enumerate(tasks,1):
        s = "[x]" if task["done"] else "[ ]"
        print(f"{s} {idx}. {task['title']} (Priority: {task['priority']}, Deadline: {task['deadline']})")

def add_task(tasks):
    while True:
        t = input("Enter task name: ").strip()
        if not t:
            print("Invalid! Try again."); continue
        if any(task["title"].lower()==t.lower() for task in tasks):
            print("Task exists!"); continue
        tasks.append({"title":t,"done":False,"priority":choose_priority(),"deadline":choose_deadline()})
        save_tasks(tasks); print("Task added!")
        show_tasks(tasks); break

def delete_task(tasks):
    if not require_tasks(tasks): return
    while True:
        show_tasks(tasks)
        try: n=int(input("Task number to delete: "))
        except: print("Invalid!"); continue
        if n<1 or n>len(tasks): print("Wrong number!"); continue
        if input(f"Delete '{tasks[n-1]['title']}'? (y/n): ").lower()=="y":
            tasks.pop(n-1); save_tasks(tasks); print("Deleted!"); break
        else: print("Cancelled!"); break

def complete_task(tasks):
    if not require_tasks(tasks): return
    while True:
        show_tasks(tasks)
        try: n=int(input("Task number to complete: "))
        except: print("Invalid!"); continue
        if n<1 or n>len(tasks): print("Wrong number!"); continue
        task=tasks[n-1]
        if task["done"]: print("Already done!"); continue
        if input(f"Complete '{task['title']}'? (y/n): ").lower()=="y":
            task["done"]=True; save_tasks(tasks); print("Marked done!"); show_tasks(tasks); break
        else: print("Cancelled!"); break

def revert_task(tasks):
    if not require_tasks(tasks): return
    while True:
        show_tasks(tasks)
        try: n=int(input("Task number to revert: "))
        except: print("Invalid!"); continue
        if n<1 or n>len(tasks): print("Wrong number!"); continue
        task=tasks[n-1]
        if not task["done"]: print("Already pending!"); continue
        if input(f"Revert '{task['title']}'? (y/n): ").lower()=="y":
            task["done"]=False; save_tasks(tasks); print("Reverted!"); show_tasks(tasks); break
        else: print("Cancelled!"); break

def edit_task(tasks):
    if not require_tasks(tasks): return
    while True:
        show_tasks(tasks)
        try: n=int(input("Task number to edit: "))
        except: print("Invalid!"); continue
        if n<1 or n>len(tasks): print("Wrong number!"); continue
        task=tasks[n-1]
        nt=input("New task name (blank to keep): ").strip()
        if nt: 
            if any(t["title"].lower()==nt.lower() for t in tasks if t!=task): print("Name exists!"); continue
            task["title"]=nt
        print(f"Current priority: {task['priority']}")
        task["priority"]=choose_priority()
        print(f"Current deadline: {task['deadline']}")
        task["deadline"]=choose_deadline()
        save_tasks(tasks); print("Task edited!"); show_tasks(tasks); break

# ---------------------- Main ----------------------

def main():
    tasks=load_tasks()
    while True:
        print("--- Task Manager ---\n1: Show\n2: Add\n3: Delete\n4: Complete\n5: Revert\n6: Edit\n7: Exit")
        c=input("Select action: ").strip()
        if c=="1": show_tasks(tasks)
        elif c=="2": add_task(tasks)
        elif c=="3": delete_task(tasks)
        elif c=="4": complete_task(tasks)
        elif c=="5": revert_task(tasks)
        elif c=="6": edit_task(tasks)
        elif c=="7": print("Exiting..."); break
        else: print("Invalid choice!")

if __name__=="__main__":
    main()