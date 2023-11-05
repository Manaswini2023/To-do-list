import tkinter as tk
from tkinter import simpledialog

class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.heading_label = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
        self.heading_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
        self.task_listbox.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_as_completed)
        self.complete_button.grid(row=2, column=2, padx=10, pady=10)
        
        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=3, column=2, padx=10, pady=10)
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=4, column=2, padx=10, pady=10)

        self.show_tasks()
        
    def add_task(self):
        task_name = simpledialog.askstring("Task Name", "Enter task name:")
        task_description = simpledialog.askstring("Task Description", "Enter task description:")
        if task_name:
            due_date = simpledialog.askstring("Due Date", "Enter due date (optional):")
            priority = simpledialog.askstring("Priority", "Enter priority (optional):")
            self.tasks.append(Task(task_name, task_description, due_date, priority))
            self.task_entry.delete(0, tk.END)
            self.show_tasks()
        
    def mark_task_as_completed(self):
        selected_task_indices = self.task_listbox.curselection()
        if selected_task_indices:
            for index in selected_task_indices:
                index = int(index)
                self.tasks[index].mark_as_completed()
            self.show_tasks()

    def edit_task(self):
        selected_task_indices = self.task_listbox.curselection()
        if selected_task_indices:
            index = int(selected_task_indices[0])
            task_name = self.tasks[index].name
            task_description = self.tasks[index].description
            edited_name = simpledialog.askstring("Edit Task Name", "Edit Task Name:", initialvalue=task_name)
            edited_description = simpledialog.askstring("Edit Task Description", "Edit Task Description:", initialvalue=task_description)
            if edited_name:
                self.tasks[index].name = edited_name
                self.tasks[index].description = edited_description
                self.show_tasks()

    def remove_task(self):
        selected_task_indices = self.task_listbox.curselection()
        if selected_task_indices:
            index = int(selected_task_indices[0])
            removed_task = self.tasks.pop(index)
            self.show_tasks()
        
    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "✔" if task.completed else " "
            name = task.name
            description = task.description
            due_date = task.due_date
            priority = task.priority
            self.task_listbox.insert(tk.END, f"{i + 1}. [{status}] {name} - {description} (Due: {due_date}, Priority: {priority})")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
