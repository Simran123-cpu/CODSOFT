import json
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Define the main task list
tasks = []

# Create a SQLite database and a tasks table
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        status BOOLEAN
    )
""")
conn.commit()

# Function to add a new task
def add_task():
    task_name = entry_task.get()
    if task_name:
        status = False  # Default status is "Not Done"
        cursor.execute("INSERT INTO tasks (name, status) VALUES (?, ?)", (task_name, status))
        conn.commit()
        load_tasks()  # Reload tasks from the database after adding a new one
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task name.")

# Function to create a string representation of a task
def create_task_string(task):
    status_str = "Done" if task["status"] else "Not Done"
    return f"[{status_str}] {task['name']}"

# Function to update task status
def update_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task = tasks[task_index]
        task["status"] = not task["status"]  # Toggle the status
        cursor.execute("UPDATE tasks SET status=? WHERE id=?", (task["status"], task["id"]))
        conn.commit()
        load_tasks()  # Reload tasks from the database after updating
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Function to delete a task
def delete_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task = tasks[task_index]
        cursor.execute("DELETE FROM tasks WHERE id=?", (task["id"],))
        conn.commit()
        load_tasks()  # Reload tasks from the database after deleting
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to load tasks from the database
def load_tasks():
    global tasks
    cursor.execute("SELECT id, name, status FROM tasks")
    task_data = cursor.fetchall()
    tasks = [{"id": task[0], "name": task[1], "status": bool(task[2])} for task in task_data]
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, create_task_string(task))
    messagebox.showinfo("Info", "Tasks loaded successfully!")
# ...

# Function to save tasks to a JSON file
def save_tasks_to_json():
    with open("tasks.json", "w") as file:
        task_data = [{"name": task["name"], "status": task["status"]} for task in tasks]
        json.dump(task_data, file)
    messagebox.showinfo("Info", "Tasks saved to JSON successfully!")

# 


# Rest of the code remains the same...

# Create the main window
window = tk.Tk()
window.title("To-Do List Application")

# Set the background color to black
window.configure(bg="black")

# Entry widget to add tasks
entry_task = tk.Entry(window, width=40, bg="black", fg="white", font=("Helvetica", 12))
entry_task.pack()

# Add Task button
add_button = tk.Button(window, text="Add Task", width=40, command=add_task, bg="blue", fg="white", font=("Helvetica", 12))
add_button.pack()

# Listbox to display tasks
listbox_tasks = tk.Listbox(window, width=40, bg="black", fg="white", font=("Helvetica", 12))
listbox_tasks.pack()

# Update Task button
update_button = tk.Button(window, text="Toggle Task Status", width=40, command=update_task, bg="green", fg="white", font=("Helvetica", 12))
update_button.pack()

# Delete Task button
delete_button = tk.Button(window, text="Delete Task", width=40, command=delete_task, bg="red", fg="white", font=("Helvetica", 12))
delete_button.pack()

# Save and Load buttons
save_button = tk.Button(window, text="Save Tasks to JSON", width=20, command=save_tasks_to_json, bg="purple", fg="white", font=("Helvetica", 12))
save_button.pack()

# Start the tkinter main loop
window.mainloop()

# Close the database connection
conn.close()

