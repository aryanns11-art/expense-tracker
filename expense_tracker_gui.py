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

#----------------------------------------------------Frames----------------------------------------------------------------------------------------

app = ctk.CTk()
app.title("Expense Tracker")
app.geometry("700x750")
app.resizable(False,False)

title = ctk.CTkLabel(app,text="Expense Tracker",font=("Arial", 28, "bold"))
title.pack(pady=20)
summary_frame = ctk.CTkFrame(app)
summary_frame.pack(fill="x", padx=10, pady=5)

input_frame = ctk.CTkFrame(app)
input_frame.pack(fill="x", padx=10, pady=5)

list_frame = ctk.CTkFrame(app)
list_frame.pack(fill="x", padx=10, pady=5)

action_frame = ctk.CTkFrame(app)
action_frame.pack(fill="x", padx=10, pady=5)

button_frame = ctk.CTkFrame(action_frame)
button_frame.pack(pady=5)

month_frame = ctk.CTkFrame(action_frame)
month_frame.pack(pady=10)

category_frame = ctk.CTkFrame(action_frame)
category_frame.pack(pady=10)

#---------------------------------------Input Frame-----------------------------------

amount_entry = ctk.CTkEntry(input_frame,placeholder_text="Enter Amount",width=250)
amount_entry.pack(fill="both",padx=5,pady=10)

category_entry = ctk.CTkEntry(input_frame,placeholder_text = "Enter Category" , width = 250)
category_entry.pack(fill="both",padx=5,pady=10)

#-----------------------------------Add Expense-------------------------------------------------------------

def add_expense():

    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showwarning("Warning","Pls enter a valid amount")
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

amount_entry.bind("<Return>",lambda event: category_entry.focus())
category_entry.bind("<Return>",lambda event: add_expense())

add_button = ctk.CTkButton(input_frame,text="Add Expense",command=add_expense, width=200,height=40)
add_button.pack(pady=15)

#------------------------------------------------------------View List-------------------------------------------------------------------------------------
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

scrollbar = ctk.CTkScrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

expense_list = Listbox(list_frame,height=10,width=70,font=("Arial", 12), bg="#2b2b2b",fg="white",selectbackground="#1f6aa5", selectforeground="white")
expense_list.pack(fill="both",expand=True,padx=20,pady=20)

expense_list.config(yscrollcommand=scrollbar.set)
scrollbar.configure(command=expense_list.yview)

#--------------------------------------------------------Total----------------------------------------------------------------------------------------
def show_total_spending():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    total_label.configure(text=f"Total Spending: ₹{total}")


total_label = ctk.CTkLabel(summary_frame,text="Total Spending: ₹0",font=("Arial",16,"bold"))
total_label.pack(pady=10)

#-------------------------------------------------------Delete Expense---------------------------------------------------------------------------------------

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

delete_button = ctk.CTkButton(button_frame,text="Delete Expense",command=delete_expense  )
delete_button.pack(side="left",padx=10)

#--------------------------------------------------------Edit Expense--------------------------------------------------------------------------------------

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
                "Pls Enter a valid Amount"
            )
            return

    save_button = ctk.CTkButton(edit_window,text="Save Changes",command=save_changes)
    save_button.pack(pady=10)
    
edit_button = ctk.CTkButton(button_frame,text="Edit Expense",command=edit_expense)
edit_button.pack(side="left",padx=10)

#-------------------------------------------------------Monthly Expense---------------------------------------------------------------------------------------
month_label = ctk.CTkLabel(month_frame,text="Filter Expenses")

month_label.pack(side="left", padx=10)
month_entry = ctk.CTkEntry(month_frame, placeholder_text="Month")
year_entry = ctk.CTkEntry(month_frame, placeholder_text="Year")

month_entry.pack(side="left", padx=5, pady=5)
year_entry.pack(side="left", padx=5, pady=5)

def view_expense_by_month():

    month = month_entry.get()
    year = year_entry.get()

    expense_list.delete(0, "end")

    for expense in expenses:

        if (expense["month"].lower() == month.lower()and expense["year"] == year):

            expense_list.insert(
                "end",
                f"{expense['date']} | "
                f"{expense['category']} | "
                f"₹{expense['amount']}"
            )
view_month_button = ctk.CTkButton(month_frame,text="View By Month",command=view_expense_by_month)
view_month_button.pack(side="left",padx=5)

show_all_button = ctk.CTkButton(month_frame,text="Show All",command=view_all_expenses)
show_all_button.pack(side="left", padx=5)

#-------------------------------------------------------Category Expense---------------------------------------------------------------------------------------
category_label = ctk.CTkLabel(category_frame,text="Category Analysis")

category_label.pack(side="left", padx=10)
category_total_entry = ctk.CTkEntry(category_frame,placeholder_text="Enter Category")
category_total_entry.pack(side="left",padx=5,pady=5)

def category_total():
    
    category = category_total_entry.get()

    if not category:
     messagebox.showwarning("Warning","Please enter a category.")
     return

    total = 0
    found = False

    for expense in expenses:

        if expense["category"].lower() == category.lower():
            total += expense["amount"]
            found = True

    if not found:
        messagebox.showinfo(
        "Category Total",
        f"No expenses found for '{category}'"
        )

    else:
        messagebox.showinfo(
            "Category Total",
            f"Total for {category}: ₹{total}"
        )

category_total_button = ctk.CTkButton(category_frame,text="Category Total",command=category_total)
category_total_button.pack(side="left",padx=5,pady=5)        

#----------------------------------------------------------------------------------------------------------------------------------------------

view_all_expenses()
app.mainloop()