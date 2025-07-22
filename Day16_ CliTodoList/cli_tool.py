import argparse
import os
from colorama import Fore, Style, init

init(autoreset=True)

TODO_FILE = "todo.txt"

def add_task(task):
    with open(TODO_FILE, "a", encoding="utf-8") as f:
        f.write(task + "\n")
    print(Fore.GREEN + f"Task added: {task}")

def view_tasks():
    if not os.path.exists(TODO_FILE):
        print(Fore.YELLOW + "No tasks found.")
        return
    print(Fore.CYAN + "Your To-Do List:")
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):
            print(Fore.CYAN + f"{idx}. {line.strip()}")

def delete_task(index):
    if not os.path.exists(TODO_FILE):
        print(Fore.RED + "No tasks to delete.")
        return
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        tasks = f.readlines()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        with open(TODO_FILE, "w", encoding="utf-8") as f:
            f.writelines(tasks)
        print(Fore.RED + f"Deleted task: {removed.strip()}")
    else:
        print(Fore.RED + "Invalid task number.")

def export_tasks(filename="todo_export.txt"):
    if not os.path.exists(TODO_FILE):
        print(Fore.YELLOW + "No tasks to export.")
        return
    with open(TODO_FILE, "r", encoding="utf-8") as src, open(filename, "w", encoding="utf-8") as dst:
        dst.writelines(src.readlines())
    print(Fore.GREEN + f"Tasks exported to {filename}")

def main():
    parser = argparse.ArgumentParser(
        description="Simple CLI To-Do List Manager",
        epilog="Example usage:\n  python cli_tool.py add \"Buy groceries\"\n  python cli_tool.py view\n  python cli_tool.py delete 2\n  python cli_tool.py export tasks.txt",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("task", type=str, help="Task description")

    # View command
    subparsers.add_parser("view", help="View all tasks")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task by its number")
    parser_delete.add_argument("index", type=int, help="Task number to delete")

    # Export command
    parser_export = subparsers.add_parser("export", help="Export tasks to a text file")
    parser_export.add_argument("--filename", type=str, default="todo_export.txt", help="Export filename (default: todo_export.txt)")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "view":
        view_tasks()
    elif args.command == "delete":
        delete_task(args.index)
    elif args.command == "export":
        export_tasks(args.filename)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()