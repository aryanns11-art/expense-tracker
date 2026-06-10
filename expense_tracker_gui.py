import json
import os
import datetime as dt
from tkinter import Listbox
import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

FILE = "expenses.json"
CATEGORY_FILE = "categories.json"

expenses = []

def save_expenses():
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)     #json.dump() ->  Converts Python data → JSON file | indent=4 -> Makes JSON readable

def save_categories():
    with open(CATEGORY_FILE, "w") as file:
        json.dump(categories, file, indent=4)

#--------------------------------------------------------------------------------------------------------------------------------------------

def load_expenses():
    global expenses

    if os.path.exists(FILE):

        try:
            with open(FILE, "r") as file:
                expenses = json.load(file)          # Reads JSON data from the file and converts it into Python objects.

        except json.JSONDecodeError:
            expenses = []

def load_categories():
    global categories

    if os.path.exists(CATEGORY_FILE):

        try:
            with open(CATEGORY_FILE, "r") as file:
                categories = json.load(file)

        except json.JSONDecodeError:
            categories = []

    else:
        categories = []            

#--------------------------------------------------------------------------------------------------------------------------------------------

load_expenses()
load_categories()

#----------------------------------------------------Frames----------------------------------------------------------------------------------------

app = ctk.CTk()
app.title("Expense Tracker")
app.geometry("1000x750")
#app.resizable(False,False)

title = ctk.CTkLabel(app,text="Expense Tracker",font=("Arial", 28, "bold"))
title.pack(pady=20)

main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=10, pady=5)
 
left_frame = ctk.CTkFrame(main_frame)
left_frame.pack_propagate(False)

right_frame = ctk.CTkFrame(main_frame)

main_frame.columnconfigure(0, weight=4)  # LEFT bigger
main_frame.columnconfigure(1, weight=3)  # RIGHT bigger than before

main_frame.rowconfigure(0, weight=1)

left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

summary_frame = ctk.CTkFrame(left_frame)
summary_frame.pack(fill="x", padx=10, pady=5)

input_frame = ctk.CTkFrame(left_frame)
input_frame.pack(fill="x", padx=10, pady=5)

list_frame = ctk.CTkFrame(left_frame)
list_frame.pack(fill="x", padx=10, pady=5)

action_frame = ctk.CTkFrame(left_frame)
action_frame.pack(fill="x", padx=10, pady=5)

button_frame = ctk.CTkFrame(action_frame)
button_frame.pack(pady=5)

month_frame = ctk.CTkFrame(action_frame)
month_frame.pack(pady=10)

category_frame = ctk.CTkFrame(action_frame)
category_frame.pack(pady=10)

graph_title = ctk.CTkLabel(right_frame, text="Analytics", font=("Arial", 18, "bold"))
graph_title.pack(pady=10)

current_canvas = None
#---------------------------------------Input Frame-----------------------------------

amount_entry = ctk.CTkEntry(input_frame,placeholder_text="Enter Amount",width=250)
amount_entry.pack(fill="both", padx=5, pady=10)

category_entry = ctk.CTkEntry(input_frame,placeholder_text="Add New Category",width=250)
category_entry.pack(fill="both", padx=5, pady=5)

category_dropdown = ctk.CTkOptionMenu(input_frame,values=["Select Category"] + categories,width=250)
category_dropdown.set("Select Category")
category_dropdown.pack(fill="x", padx=5, pady=5)

def add_category():

    category = category_entry.get().strip()

    if category == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a category."
        )
        return

    if category in categories:
        messagebox.showwarning(
            "Warning",
            "Category already exists."
        )
        return

    categories.append(category)
    save_categories()
    category_dropdown.configure(values=["Selct Category"]+categories)
    category_entry.delete(0, "end")

    messagebox.showinfo(
        "Success",
        f"'{category}' added."
    )

add_category_button = ctk.CTkButton(input_frame,text="Add Category",command=add_category)
add_category_button.pack(pady=5)

#-----------------------------------Add Expense-------------------------------------------------------------

def add_expense():

    try:
        amount = float(amount_entry.get())
        category = category_dropdown.get()
    
    except ValueError:
        messagebox.showwarning("Warning","Pls enter a valid amount")
        return

    category = category_dropdown.get()

    if category == "Select Category":
        messagebox.showwarning(
        "Warning",
        "Please select a category."
        )
        return

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
    category_dropdown.set("Select Category")
    amount_entry.focus()

amount_entry.bind("<Return>",lambda event: category_entry.focus())
category_entry.bind("<Return>",lambda event: add_category())

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
    
    edit_window.transient(app)   # Associate with main window
    edit_window.grab_set()       # Make it modal
    edit_window.focus_force()    # Bring to front

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

def category_total():
    
    category = category_dropdown.get()

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

def show_category_chart():
    global current_canvas

    category_data = {}

    for expense in expenses:
        cat = expense["category"]
        category_data[cat] = category_data.get(cat, 0) + expense["amount"]

    if not category_data:
        messagebox.showwarning("Warning", "No data to show.")
        return

    if current_canvas is not None:
        current_canvas.get_tk_widget().pack_forget()
        current_canvas.get_tk_widget().destroy()

    fig, ax = plt.subplots(figsize=(4,3))
    ax.bar(category_data.keys(), category_data.values())

    ax.set_title("Expenses by Category")
    ax.set_ylabel("Amount")

    current_canvas = FigureCanvasTkAgg(fig, master=right_frame)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack(fill="both", expand=True, pady=10)

    
graph_button = ctk.CTkButton(right_frame,text="Show Category Chart",command=show_category_chart)
graph_button.pack(pady=10)

#---------------------------------------------------------------------------------------------------------------------------------------------    
view_all_expenses()

def on_closing():
    try:
        app.quit()
        app.destroy()
    except:
        pass

app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()