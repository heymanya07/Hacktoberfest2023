import tkinter as tk
from tkinter import messagebox
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main application window
app = tk.Tk()
app.title("To-Do List Manager")

# Create and configure the task entry field
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)
task_entry.focus()

# Create and configure the "Add Task" button
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

# Create and configure the task list
task_list = tk.Listbox(app, selectbackground="yellow", selectmode=tk.SINGLE, height=10, width=40)
task_list.pack(pady=10)

# Create and configure the "Remove Task" button
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack()

# Start the Tkinter event loop
app.mainloop()
