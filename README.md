# TODO-CLI

A simple Command Line Todo Application built using Python and argparse.
It allows you to add tasks, list pending/completed tasks, and mark tasks as done using the terminal.
🚀 Features
✅ Add new tasks
📋 List all tasks
Completed tasks
Pending tasks
✔ Mark tasks as done
💾 Persistent storage using JSON
🐍 Built with Python standard library only

Project Structure

├── cli.py        # Main CLI application
├── task.json     # Task storage (auto-created)
└── README.md

⚙️ Requirements
Python 3.8+
No external dependencies

▶️ Usage
Run all commands using:
python3 cli.py <command> [arguments]

➕ Add a Task
python3 cli.py add "Buy groceries"
Output:
Task added

📋 List Tasks
python3 cli.py list
Output Example:
------------------
|   Done Task    |
------------------
1. Morning walk

------------------
| To be Done Task |
------------------
1. Buy groceries
2. Learn Python

✔ Mark Task as Done
The done command works on pending tasks only.
python3 cli.py done 1
Output:
Task Updated

🗂 task.json Format
Tasks are stored in a JSON file:
[
  {
    "task": "Buy groceries",
    "done": false
  },
  {
    "task": "Morning walk",
    "done": true
  }
]


🧠 How It Works
Uses argparse for CLI commands
Uses json for persistent storage
Uses task IDs based on pending task order
Automatically handles missing or empty files
🛠 Future Improvements
❌ Delete task
⏰ Due dates
⭐ Priority levels
🎨 Colored output
📦 Install as a global command (todo)
🧪 Unit tests


