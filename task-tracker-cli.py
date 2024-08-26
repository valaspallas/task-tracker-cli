import argparse
import os
import json
from datetime import datetime

# Set up the argument parser
parser = argparse.ArgumentParser(description="ClI Task Tracker", formatter_class=argparse.RawTextHelpFormatter)

# Define the actions and arguments
parser.add_argument(
    "action",
    type=str,
    choices=[
        "add",
        "update",
        "delete",
        "mark_in_progress",
        "mark_done",
        "list_all",
        "list_done",
        "list_not_done",
        "list_in_progress"
    ],
        help="""Choose an action:
        add                     - Add a new task
        update                  - Update an existing task
        delete                  - Delete a task
        mark_in_progress        - Mark a task as in progress
        mark_done               - Mark a task as done
        list_all                - List all tasks
        list_done               - List all done tasks
        list_not_done           - List all not done tasks
        list_in_progress        - List all tasks in progress"""
)

parser.add_argument("description_or_id", type=str, nargs='?', help="Description of the task for 'add' action or ID of the task for other actions")
parser.add_argument("new_description", type=str, nargs='?', help="New description for the 'update' action")

args = parser.parse_args()

file_path = 'tasks.json'
formatted_time = datetime.now().isoformat()

# Create the initial JSON file if it doesn't exist
def create_initial_json():
    initial_data = {
        "counter": 0,
        "tasks": []
    }
    with open(file_path, 'w') as file:
        json.dump(initial_data, file, indent=4)
    print("Initialized tasks.json with counter 0")

# Load tasks from the JSON file
def load_tasks():
    if not os.path.exists(file_path):
        create_initial_json()
    with open(file_path, 'r') as file:
        return json.load(file)

# Save tasks to the JSON file
def save_tasks(data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Tasks saved to {file_path}")

# Add a new task
def add_task(description):
    if not description:
        print("Error: Task description cannot be empty.")
        return
    data = load_tasks()
    data["counter"] += 1
    new_task = {
        'id': data["counter"],
        'description': description,
        'status': 'todo',
        'createdAt': formatted_time,
        'updatedAt': formatted_time
    }
    data["tasks"].append(new_task)
    save_tasks(data)
    print(f"Task added (ID: {new_task['id']})")

# Update an existing task
def update_task(task_id, description):
    data = load_tasks()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = formatted_time
            save_tasks(data)
            print(f"Task {task_id} updated")
            return
    print(f"Task {task_id} not found")

# Delete task by ID
def delete_task(task_id):
    data = load_tasks()
    initial_task_count = len(data["tasks"])
    data["tasks"] = [task for task in data["tasks"] if task["id"] != task_id]
    if len(data["tasks"]) < initial_task_count:
        save_tasks(data)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Task {task_id} not found")

# Mark a task with status
def mark_task(task_id, status):
    data = load_tasks()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = formatted_time
            save_tasks(data)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")

# List tasks, optionally by status
def list_tasks(status=None):
    data = load_tasks()
    tasks = data["tasks"]
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

# Action handling
if args.action == "add":
    add_task(args.description_or_id)
elif args.action == "update":
    if args.description_or_id and args.new_description:
        update_task(int(args.description_or_id), args.new_description)
    else:
        print("Task ID and new description are required for this action")
elif args.action == "delete":
    if args.description_or_id:
        delete_task(int(args.description_or_id))
    else:
        print("Task ID is required for this action")
elif args.action == "mark_in_progress":
    if args.description_or_id:
        mark_task(int(args.description_or_id), "in-progress")
    else:
        print("Task ID is required for this action")
elif args.action == "mark_done":
    if args.description_or_id:
        mark_task(int(args.description_or_id), "done")
    else:
        print("Task ID is required for this action")
elif args.action == "list_all":
    list_tasks()
elif args.action == "list_done":
    list_tasks("done")
elif args.action == "list_not_done":
    list_tasks("todo")
elif args.action == "list_in_progress":
    list_tasks("in-progress")
else:
    print("Unknown action")

