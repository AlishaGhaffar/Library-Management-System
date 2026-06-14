
# 📚 Library Management System

A simple console-based Library Management System built using Python.  
This project helps manage books efficiently using core Python concepts like lists, dictionaries, loops, and functions.

---

## 🚀 Features

- ➕ Add new books with unique ID  
- 🔍 Search books by title  
- 📖 View all books with status  
- 📤 Issue books  
- 📥 Return books  
- ❌ Remove books  
- 🆔 Book ID system  
- ⚠️ Input validation (duplicate ID / empty fields)  
- 📊 Book status tracking (Available / Issued)

---

## 🛠️ Tech Stack

- Python (Core Python only)  
- No external libraries  
- No database (in-memory storage using lists & dictionaries)

---

## ▶️ How to Run

1. Make sure Python is installed  
2. Clone or download this repository  
3. Open terminal in project folder  
4. Run the program:

```bash
python main.py
💡 How It Works

Each book is stored as a dictionary:

{
    "id": "101",
    "title": "Python Basics",
    "author": "Ali Khan",
    "status": "Available"
}

All books are stored in a list:

books = []
📸 Example Output
==============================
 Library Management System
==============================
1. Add Book
2. Search Book
3. View All Books
4. Issue Book
5. Return Book
6. Remove Book
7. Exit
🎯 Learning Objectives

This project helps in understanding:

Python functions
Loops and conditionals
Lists and dictionaries
Input validation
Basic problem solving
Menu-driven programs


🔥 Future Improvements
File handling (save data permanently)
User login system (Admin/Student)
Due date & fine system
GUI version using Tkinter
Database integration (SQLite/MySQL)


👨‍💻 Author
Alisha Ghaffar

📌 Note
This is a beginner-friendly project built for learning Python fundamentals and logic building.