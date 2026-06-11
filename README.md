# 💰 Expense Tracker

A modern desktop Expense Tracker application built using **Python**, **CustomTkinter**, and **Matplotlib**. It helps users manage expenses, organize spending categories, track monthly expenses, and visualize financial data through interactive charts.

# 🚀 Features

- 💸 Add new expenses
- 🗂️ Create and manage custom categories
- 📋 View all recorded expenses
- ✏️ Edit existing expenses
- 🗑️ Delete expenses
- 📅 Filter expenses by month and year
- 📊 Calculate category-wise spending totals
- 📈 Visualize expenses using bar charts
- 💾 Store data locally using JSON files
- 🎨 Modern GUI built with CustomTkinter
- 🕒 Automatic date and time tracking

# 🛠️ Technologies Used

- Python
- CustomTkinter
- Tkinter
- JSON
- Matplotlib

# 📂 Project Structure

```text
expense-tracker/
│
├── expense_tracker.py
├── expenses.json
├── categories.json
└── README.md
```

# 📸 Application Modules

## Expense Management

- Add expenses with amount and category
- Edit existing expenses
- Delete expenses
- View complete expense history

## Category Management

- Create custom categories
- Prevent duplicate categories
- Analyze category-wise spending

## Analytics Dashboard

- Display total spending summary
- Category expenditure analysis
- Interactive bar chart visualization

## Monthly Filtering

- Filter expenses by month and year
- View spending records for specific periods

# 📊 Data Storage

The application stores data locally using JSON files.

### Example Expense Record

```json
{
    "amount": 500,
    "category": "Food",
    "date": "10-06-2026",
    "time": "14:30:22",
    "month": "June",
    "year": "2026"
}
```

### Example Categories

```json
[
    "Food",
    "Travel",
    "Shopping"
]
```

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

## Install Dependencies

```bash
pip install customtkinter matplotlib pillow
```

## Run Application

```bash
python expense_tracker.py
```

# 🎯 Future Improvements

- 🔍 Search expenses
- 📄 Export reports to PDF or Excel
- 🌙 Dark/Light mode toggle
- 📉 Monthly trend analytics
- 🏦 Budget planning system
- 🔐 User authentication

# 👨‍💻 Author

**Aryan**

Diploma Student | Python Developer | Tech Enthusiast

Passionate about software development, machine learning, and building practical applications using Python.

# ⭐ Support

If you found this project useful, consider giving it a star on GitHub and sharing it with others.