import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def mark_as_incomplete(self):
        self.completed = False

    def update(self, title=None, description=None, due_date=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date

    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def update_task(self, index, title=None, description=None, due_date=None):
        if 0 <= index < len(self.tasks):
            self.tasks[index].update(title, description, due_date)

    def mark_task_as_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_complete()

    def mark_task_as_incomplete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_incomplete()

    def get_tasks(self, status=None):
        if status == "complete":
            return [task for task in self.tasks if task.completed]
        elif status == "incomplete":
            return [task for task in self.tasks if not task.completed]
        return self.tasks

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = ToDoList()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = tk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.complete_button = tk.Button(self.frame, text="Mark Complete", command=self.mark_task_complete)
        self.complete_button.grid(row=0, column=3, padx=5)

        self.incomplete_button = tk.Button(self.frame, text="Mark Incomplete", command=self.mark_task_incomplete)
        self.incomplete_button.grid(row=0, column=4, padx=5)

        self.status_var = tk.StringVar(value="all")
        self.status_menu = tk.OptionMenu(self.frame, self.status_var, "all", "complete", "incomplete", command=self.view_tasks)
        self.status_menu.grid(row=0, column=5, padx=5)

        self.tasks_listbox = tk.Listbox(self.root, width=50, height=15)
        self.tasks_listbox.pack(pady=10)
        
        self.view_tasks()

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            description = simpledialog.askstring("Add Task", "Enter task description:")
            due_date_str = simpledialog.askstring("Add Task", "Enter due date (YYYY-MM-DD):")
            try:
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
                task = Task(title, description, due_date)
                self.todo_list.add_task(task)
                self.view_tasks()
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
    
    def update_task(self):
        index = self.tasks_listbox.curselection()
        if index:
            index = index[0]
            task = self.todo_list.tasks[index]
            title = simpledialog.askstring("Update Task", "Enter new title:", initialvalue=task.title)
            description = simpledialog.askstring("Update Task", "Enter new description:", initialvalue=task.description)
            due_date_str = simpledialog.askstring("Update Task", "Enter new due date (YYYY-MM-DD):", initialvalue=str(task.due_date))
            try:
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
                self.todo_list.update_task(index, title, description, due_date)
                self.view_tasks()
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
        else:
            messagebox.showwarning("No Selection", "Please select a task to update.")

    def delete_task(self):
        index = self.tasks_listbox.curselection()
        if index:
            index = index[0]
            self.todo_list.delete_task(index)
            self.view_tasks()
        else:
            messagebox.showwarning("No Selection", "Please select a task to delete.")

    def mark_task_complete(self):
        index = self.tasks_listbox.curselection()
        if index:
            index = index[0]
            self.todo_list.mark_task_as_complete(index)
            self.view_tasks()
        else:
            messagebox.showwarning("No Selection", "Please select a task to mark as complete.")

    def mark_task_incomplete(self):
        index = self.tasks_listbox.curselection()
        if index:
            index = index[0]
            self.todo_list.mark_task_as_incomplete(index)
            self.view_tasks()
        else:
            messagebox.showwarning("No Selection", "Please select a task to mark as incomplete.")

    def view_tasks(self, status=None):
        self.tasks_listbox.delete(0, tk.END)
        status = self.status_var.get()
        tasks = self.todo_list.get_tasks(status)
        for task in tasks:
            self.tasks_listbox.insert(tk.END, f"{task.title} ({task.due_date}) - {'Complete' if task.completed else 'Incomplete'}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
