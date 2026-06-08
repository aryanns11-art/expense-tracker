# 💰 Expense Tracker (CustomTkinter)

A modern desktop Expense Tracker application built with **Python** and **CustomTkinter**.

This application helps users manage their daily expenses with a clean graphical interface and persistent JSON-based storage.

---

# 🚀 Features

* ➕ Add new expenses
* 📋 View all recorded expenses
* ✏️ Edit existing expenses
* ❌ Delete expenses
* 📅 Filter expenses by Month and Year
* 📊 View category-wise spending totals
* 💰 Display total spending automatically
* 💾 Persistent data storage using JSON
* 🎨 Modern GUI built with CustomTkinter
* 🔄 Real-time updates without restarting the application

---

# 🛠️ Technologies Used

* Python
* CustomTkinter
* Tkinter
* JSON
* Datetime
* OS Module

---

# 📂 Project Structure

```text
expense-tracker/
│
├── main.py
├── expenses.json
└── README.md
```

---

# 📸 Application Features

### Add Expense

Users can enter:

* Expense Amount
* Expense Category

and save the expense instantly.

### View Expenses

All saved expenses are displayed in a list with:

* Date
* Category
* Amount

### Edit Expense

Modify existing expense records through a popup window.

### Delete Expense

Remove selected expenses from the tracker.

### Monthly Filter

View expenses for a specific month and year.

### Category Analysis

Calculate total spending for a particular category.

### Total Spending

Displays the total amount spent across all recorded expenses.

---

# 💾 Data Storage

All expense data is stored locally in:

```text
expenses.json
```

Example:

```json
[
    {
        "amount": 250,
        "category": "Food",
        "date": "08-06-2026",
        "time": "14:30:20",
        "month": "June",
        "year": "2026"
    }
]
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project folder:

```bash
cd expense-tracker
```

Install CustomTkinter:

```bash
pip install customtkinter
```

Run the application:

```bash
python main.py
```

---

# 🎯 Future Improvements

* 📈 Expense charts and graphs
* 📤 Export data to CSV
* 🔍 Search expenses
* 🌙 Light/Dark theme switch
* 📊 Monthly summary dashboard

---

# 👨‍💻 Author

Aryan

Built as a Python GUI project to practice:

* File Handling
* JSON
* Tkinter / CustomTkinter
* GUI Design
* CRUD Operations
* Data Management
