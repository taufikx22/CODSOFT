import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.task_listbox.bind("<Double-Button-1>", lambda event: self.update_task)

        root.rowconfigure(1, weight=1)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_list()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            updated_task = tk.simpledialog.askstring("Update Task", "Update task:", initialvalue=selected_task)
            if updated_task:
                self.tasks[selected_index[0]] = updated_task
                self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{i}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
