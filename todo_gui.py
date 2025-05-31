import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x300")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

root.mainloop()
