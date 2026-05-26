import datetime as dt

expenses = []
def add_expense():

    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    now = dt.datetime.now()


    expense = {
        "amount": amount,
        "category": category,
        "date": now.strftime("%d-%m-%Y"),                  # % = “insert dynamic value here” . Without % = “just print text”
        "time": now.strftime("%H:%M:%S"),                  #strftime() → formats it into readable form
        "month": now.strftime("%B"),
        "year": now.strftime("%Y")
      }
    
    expenses.append(expense)
    #save_expenses()

    print("Expense added successfully!")

def view_all_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Expenses :")
        for expense in expenses:
            print(f"{expense['date']} {expense['time']} - {expense['category']}: ₹{expense['amount']}") 

def view_expense(month, year):
    results = []

    for expense in expenses:
        if expense['month'].lower() == month.lower() and expense['year'] == year:
            results.append(expense)

    if not results:
        print(f"No expenses found for {month} {year}")
    else:
        for expense in results:
            print(f"{expense['date']} {expense['time']} - {expense['category']}: ₹{expense['amount']}")            

def category_total_input():
    category = input("Enter category: ")
    total = 0
    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]                                 
            found = True

    if not found:
        print(f"No expenses found for category '{category}'")
    else:
        print(f"Total for {category}: ₹{total}")                    


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expenses By Month")
    print("4. Category Total")
    print("5. Exit")

    choice = input("Enter choice: ")

    match choice:

        case "1":
            add_expense()

        case "2":
            view_all_expenses()

        case "3":
            month=input("Enter Month:")
            year=input("Enter Year:")
            view_expense(month,year)

        case "4":
            category_total_input()

        case "5":
            print("Exiting...")
            break

        case _:
            print("Invalid choice")        