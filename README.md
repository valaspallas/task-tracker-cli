# CLI Task Tracker

A simple command-line interface (CLI) application for tracking tasks. You can add, update, delete, and list tasks, as well as mark them as in progress or done.

## Challenge

This is a challenge from https://roadmap.sh/projects/task-tracker

## Features

- Add a new task
- Update an existing task
- Delete a task
- Mark a task as in progress
- Mark a task as done
- List all tasks
- List tasks by status (done, not done, in progress)

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository**

```sh
git clone https://github.com/valaspallas/task-tracker-cli
```

2. **Navigate to the Project Directory**

```sh
cd projects/todo
```

## Usage

Run the script with the desired action and arguments.

### Add a New Task

```sh
python todo.py add "task description"
```

### Update an existing Task

```sh
python todo.py update 2 "new task description"
```

### Delete a Task
```sh
python todo.py delete 3
```

### Mark a Task as In Progress
```sh
python todo.py mark_in_progress task_id
```

### Mark a Task as Done

```sh
python todo.py mark_done task_id
```

### List All Tasks

```sh
python todo.py list_all
```

### List Done Tasks

```sh
python todo.py list_done
```

### List Not Done Tasks

```sh
python todo.py list_not_done
```

### List Tasks In Progress

```sh
python todo.py list_in_progress
```