import argparse
import json
import os

FILE = "task.json"

# ---------- File Helpers ----------
def load_json():    
    if not os.path.exists(FILE):
        return []

    if os.path.getsize(FILE) == 0:
        return []

    with open(FILE, "r") as f:
        return json.load(f)

def write_json(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)



# ---------- Commands ----------
def list_task(args):
    tasks = load_json()

    if not tasks:
        print(" No tasks found")
        return
    
    done_task = []
    not_done_task = []
    for i, t in enumerate(tasks, 1):
        if t['done'] == False:
            not_done_task.append(t['task'])
        elif t['done'] == True:
            done_task.append(t['task'])
        
    print("------------------")
    print("|   Done Task    |")
    print("------------------")
    for i ,t in enumerate(done_task,1):
        print(f"{i}. {t}")
    print(" ")
    print(" ")
    print("------------------")
    print("| To be Done Task |")
    print("------------------")
    for i ,t in enumerate(not_done_task,1):
        print(f"{i}. {t}")
    print("")



def add_task(args):
    tasks = load_json()
    tasks.append({"task": args.task, "done": False})
    write_json(tasks)
    print(" Task added")



def done_task(args):
    tasks = load_json()
    done_task = []
    not_done_task = []
    for i, t in enumerate(tasks, 1):
        if t['done'] == False:
            not_done_task.append(t['task'])
        elif t['done'] == True:
            done_task.append(t['task'])
    if args.id > len(not_done_task) or args.id <=0:
        print(" Invalid Task ID ")
        return 
    task = not_done_task[args.id-1]
    for t in tasks:
        if t['task'] == task:
            t['done']= True
            break
    write_json(tasks)
    print("Task Updated ")


# ---------- CLI ----------
def main():
    parser = argparse.ArgumentParser(description="Today's ToDo")
    subparsers = parser.add_subparsers(dest="command")

    # add command
    add_parser = subparsers.add_parser("add", help="Adds a new task to list")
    add_parser.add_argument("task", help="Task Description")
    add_parser.set_defaults(func=add_task)

    # list command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.set_defaults(func=list_task)

    # done command 
    done_parser = subparsers.add_parser("done", help="Mark task as done")
    done_parser.add_argument("id", type=int, help="Task ID")
    done_parser.set_defaults(func=done_task)


    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()
