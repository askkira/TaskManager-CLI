import json

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

# ---------------------- Task Operations ----------------------

def show_tasks(tasks):
    if not tasks:
        print("Task list is empty!")
        return
    print("Tasks:")
    for i, t in enumerate(tasks,1):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{status} {i}. {t['title']}")

def add_task(tasks):
    while True:
        show_tasks(tasks)
        title = input("Add task (Enter to exit): ").strip()
        if not title:
            break
        if any(t["title"].lower() == title.lower() for t in tasks):
            print("Task exists!")
            continue
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        show_tasks(tasks)
        print("Task added!")

def delete_task(tasks):
    if not require_tasks(tasks): return
    while True:
        show_tasks(tasks)
        inp = input("Delete task number (Enter to exit): ").strip()
        if not inp: break
        try: n = int(inp)
        except: 
            print("Invalid number!")
            continue
        if n<1 or n>len(tasks):
            print("Out of range!")
            continue
        if input(f"Confirm delete '{tasks[n-1]['title']}'? (y/n): ").lower()!="y":
            print("Cancelled")
            break
        tasks.pop(n-1)
        save_tasks(tasks)
        show_tasks(tasks)
        print("Deleted!")

def complete_task(tasks):
    if not require_tasks(tasks): return
    while True:
        show_tasks(tasks)
        inp = input("Complete task number (Enter to exit): ").strip()
        if not inp: break
        try: n = int(inp)
        except: 
            print("Invalid number!")
            continue
        if n<1 or n>len(tasks): 
            print("Out of range!")
            continue
        if tasks[n-1]["done"]:
            print("Already done!")
            continue
        tasks[n-1]["done"]=True
        save_tasks(tasks)
        show_tasks(tasks)
        print("Marked completed!")

def revert_task(tasks):
    if not require_tasks(tasks): return
    while True:
        show_tasks(tasks)
        inp = input("Revert task number (Enter to exit): ").strip()
        if not inp: break
        try: n=int(inp)
        except:
            print("Invalid number!")
            continue
        if n<1 or n>len(tasks):
            print("Out of range!")
            continue
        if not tasks[n-1]["done"]:
            print("Already pending!")
            continue
        tasks[n-1]["done"]=False
        save_tasks(tasks)
        show_tasks(tasks)
        print("Reverted to pending!")

def edit_task(tasks):
    if not require_tasks(tasks): return
    while True:
        show_tasks(tasks)
        inp = input("Edit task number (Enter to exit): ").strip()
        if not inp: break
        try: n=int(inp)
        except:
            print("Invalid number!")
            continue
        if n<1 or n>len(tasks):
            print("Out of range!")
            continue
        new_text=input("New task text (Enter to cancel): ").strip()
        if not new_text:
            print("Cancelled")
            break
        if any(t["title"].lower()==new_text.lower() for t in tasks):
            print("Task exists!")
            continue
        tasks[n-1]["title"]=new_text
        save_tasks(tasks)
        show_tasks(tasks)
        print("Edited!")

# ---------------------- Main ----------------------

def main():
    tasks = load_tasks()
    while True:
        print("\n1.Show 2.Add 3.Delete 4.Complete 5.Revert 6.Edit 7.Exit")
        choice=input("Choose: ").strip()
        if choice=="1": show_tasks(tasks)
        elif choice=="2": add_task(tasks)
        elif choice=="3": delete_task(tasks)
        elif choice=="4": complete_task(tasks)
        elif choice=="5": revert_task(tasks)
        elif choice=="6": edit_task(tasks)
        elif choice=="7": break
        else: print("Invalid choice!")

if __name__=="__main__":
    main()