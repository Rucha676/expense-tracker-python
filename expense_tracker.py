import tkinter as tk
from tkinter import messagebox

# list to store all expenses
expenses = []

# function for add button
def add_expense():
    amt = amount_entry.get()
    cat = category_var.get()
    note = note_entry.get()
    dt = date_entry.get()

    if amt == "" or cat == "Select Category" or dt == "":
        messagebox.showwarning("Missing", "Please enter amount, category and date")
        return

    try:
        amt = float(amt)
    except:
        messagebox.showwarning("Error", "Amount must be a number")
        return

    # add expense to the list
    expenses.append((amt, cat, note, dt))
    amount_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    load_data()
    update_total()

# update the listbox with all expenses
def load_data():
    listbox.delete(0, tk.END)
    for i, (amt, cat, note, dt) in enumerate(expenses, start=1):
        listbox.insert(tk.END, f"{i}. {dt} | ₹{amt:.2f} | {cat} | {note}")

# delete selected expense
def delete_expense():
    sel = listbox.curselection()
    if not sel:
        return
    index = sel[0]
    expenses.pop(index)
    load_data()
    update_total()

# calculate total amount
def update_total():
    total = sum(amt for amt, _, _, _ in expenses)
    total_var.set(f"Total: ₹{total:.2f}")

# main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("550x500")
root.configure(bg="#f9f9f9")

# heading
tk.Label(root, text="My Expense Tracker", bg="#f9f9f9", fg="#2c3e50", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

# amount
tk.Label(root, text="Amount:", bg="#f9f9f9").grid(row=1, column=0, padx=10, pady=5, sticky="w")
amount_entry = tk.Entry(root, width=25)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

# category
tk.Label(root, text="Category:", bg="#f9f9f9").grid(row=2, column=0, padx=10, pady=5, sticky="w")
category_var = tk.StringVar(root)
category_var.set("Select Category")
categories = ["Food", "Travel", "Shopping", "Bills", "Health", "Other"]
category_menu = tk.OptionMenu(root, category_var, *categories)
category_menu.config(width=20)
category_menu.grid(row=2, column=1, padx=10, pady=5)

# note
tk.Label(root, text="Note:", bg="#f9f9f9").grid(row=3, column=0, padx=10, pady=5, sticky="w")
note_entry = tk.Entry(root, width=25)
note_entry.grid(row=3, column=1, padx=10, pady=5)

# date
tk.Label(root, text="Date:", bg="#f9f9f9").grid(row=4, column=0, padx=10, pady=5, sticky="w")
date_entry = tk.Entry(root, width=25)
date_entry.grid(row=4, column=1, padx=10, pady=5)

# buttons
tk.Button(root, text="Add Expense", command=add_expense, bg="#27ae60", fg="white", width=15).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Delete Expense", command=delete_expense, bg="#c0392b", fg="white", width=15).grid(row=5, column=1, padx=10, pady=10)

# listbox
listbox = tk.Listbox(root, width=70, height=12, bg="white", fg="black")
listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=15)

# total label
total_var = tk.StringVar(value="Total: ₹0.00")
tk.Label(root, textvariable=total_var, bg="#f9f9f9", fg="#2c3e50", font=("Arial", 12, "bold")).grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
