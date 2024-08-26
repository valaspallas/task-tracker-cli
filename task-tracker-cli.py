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

parser.add_argument("description", type=str, nargs='?', help="Description of the task")
parser.add_argument("task_id", type=int, nargs='?', help="ID of the task")

args = parser.parse_args()

file_path = 'tasks.json'
formatted_time = datetime.now().isoformat()

def create_initial_json():
    initial_data = {
        "counter": 0,
        "tasks": []
    }
    with open(file_path, 'w') as file:
        json.dump(initial_data, file, indent=4)
    print("Initialized tasks.json with counter 0")


if args.action == "add":
    create_initial_json()
elif args.action in "update":
    print("Updating a task...")
elif args.action in "delete":
    print("Deleting a task...")
elif args.action in "mark_in_progress":
    print("Marking task as in progress...")
elif args.action in "done":
    print("Marking task as done...")
elif args.action in "list_all":
    print("Listing all tasks...")
elif args.action in "list_done":
    print("Listing all done tasks...")
elif args.action in "list_not_done":
    print("Listing all not done tasks...")
elif args.action in "list_in_progress":
    print("Listing all tasks in progress...")
