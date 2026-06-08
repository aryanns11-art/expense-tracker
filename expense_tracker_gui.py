import json
import os
import datetime as dt
from tkinter import Listbox
import customtkinter as ctk
from tkinter import messagebox

FILE_NAME = "expenses.json"

expenses = []

def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)     #json.dump() ->  Converts Python data → JSON file | indent=4 -> Makes JSON readable

#--------------------------------------------------------------------------------------------------------------------------------------------

def load_expenses():
    global expenses

    if os.path.exists(FILE_NAME):

        try:
            with open(FILE_NAME, "r") as file:
                expenses = json.load(file)          # Reads JSON data from the file and converts it into Python objects.

        except json.JSONDecodeError:
            expenses = []

#--------------------------------------------------------------------------------------------------------------------------------------------

load_expenses()

#--------------------------------------------------------------------------------------------------------------------------------------------
app = ctk.CTk()
app.title("Expense Tracker")
app.geometry("400x700")
app.resizable(False,False)


title = ctk.CTkLabel(app,text="Expense Tracker",font=("Arial", 28, "bold"))
title.pack(pady=20) 

amount_entry = ctk.CTkEntry(app,placeholder_text="Enter Amount",width=250)
amount_entry.pack(fill="both",padx=5,pady=10)

category_entry = ctk.CTkEntry(app,placeholder_text = "Enter Category" , width = 250)
category_entry.pack(fill="both",padx=5,pady=10)

#------------------------------------------------------------------------------------------------

def add_expense():

    try:
        amount = float(amount_entry.get())
    except ValueError:
        print("Invalid amount")
        return

    category = category_entry.get()

    now = dt.datetime.now()

    expense = {
        "amount": amount,
        "category": category,
        "date": now.strftime("%d-%m-%Y"),                     
        "time": now.strftime("%H:%M:%S"),                     # % = “insert dynamic value here” . Without % = “just print text”
        "month": now.strftime("%B"),                          # strftime() → formats it into readable form 
        "year": now.strftime("%Y")
    }

    expenses.append(expense)
    save_expenses()
    view_all_expenses()

    messagebox.showinfo("Success","Expense Added")
    
    amount_entry.delete(0, "end")
    category_entry.delete(0, "end")
    amount_entry.focus()

amount_entry.bind("<Return>", lambda event: add_expense())
category_entry.bind("<Return>", lambda event: add_expense())

add_button = ctk.CTkButton(app,text="Add Expense",command=add_expense)
add_button.pack(pady=15)


#---------------------------------------------------------------------------------------------------------------------------------------------
def view_all_expenses():

    expense_list.delete(0, "end")

    for i, expense in enumerate(expenses, start=1):

        expense_list.insert(
            "end",
            f"{i}. | "
            f" {expense['date']} |  "
            f" {expense['category']}  | "
            f" ₹{expense['amount']}\n"
        )

    show_total_spending()    

expense_list = Listbox(app,height=12,width=50,font=("Arial", 12), bg="#2b2b2b",fg="white",selectbackground="#1f6aa5", selectforeground="white")
expense_list.pack(pady=10)

#----------------------------------------------------------------------------------------------------------------------------------------------
def show_total_spending():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    total_label.configure(text=f"Total Spending: ₹{total}")


total_label = ctk.CTkLabel(app,text="Total Spending: ₹0",font=("Arial",16,"bold"))
total_label.pack(pady=10)


#----------------------------------------------------------------------------------------------------------------------------------------------

def delete_expense():

    if not expenses:
        messagebox.showwarning("warning !","No expenses to delete.")
        return

    try:
        selected = expense_list.curselection()[0]
        deleted = expenses.pop(selected)

        save_expenses()
        view_all_expenses()

        messagebox.showinfo("Deleted Expense",f"{deleted['category']} - {deleted['amount']}")

    except IndexError:
        messagebox.showwarning("Warning !","Expense number does not exist.")  

delete_button = ctk.CTkButton(app,text="Delete Expense",command=delete_expense  )
delete_button.pack(pady=10)

#----------------------------------------------------------------------------------------------------------------------------------------------

def edit_expense():

    try:
        selected = expense_list.curselection()[0]

        expense = expenses[selected]

    except IndexError:

        messagebox.showwarning(
            "Warning",
            "Please select an expense."
        )
        return

    edit_window = ctk.CTkToplevel(app)    # Create popup window
    edit_window.title("Edit Expense")
    edit_window.geometry("300x200")

    amount_edit = ctk.CTkEntry(edit_window)   #Entry of new values
    amount_edit.pack(pady=10)
    amount_edit.insert(0, expense["amount"])

    category_edit = ctk.CTkEntry(edit_window)
    category_edit.pack(pady=10)
    category_edit.insert(0, expense["category"])

    def save_changes():

        try:
            expense["amount"] = float(amount_edit.get())
            expense["category"] = category_edit.get()

            save_expenses()
            view_all_expenses()

            messagebox.showinfo(
                "Success",
                "Expense Updated"
            )

            edit_window.destroy()

        except ValueError:

            messagebox.showwarning(
                "Warning",
                "Invalid Amount"
            )

    save_button = ctk.CTkButton(
        edit_window,
        text="Save Changes",
        command=save_changes
    )

    save_button.pack(pady=10)

#----------------------------------------------------------------------------------------------------------------------------------------------

view_all_expenses()
app.mainloop()