# 📝 My Notebook (CLI Notes App)

A simple command-line notebook application built with Python. This program allows users to create, view, update, and delete notes, with all data stored persistently in a CSV file.

---

## 📌 Features

* Create new notes with a title and content
* View all saved notes
* Update existing notes
* Delete notes
* Automatically saves notes to a CSV file (`notes.csv`)
* Loads saved notes on startup

---

## 🛠️ Technologies Used

* Python 3
* Built-in modules:

  * `datetime` (for timestamps)
  * `csv` (for file storage)
  * `os` (for file handling)

---

## 📂 File Structure

```
.
├── notes.csv       # Stores all notes (auto-generated)
└── main.py         # Main application script
```

---

## ▶️ How to Run

1. Make sure you have Python installed (Python 3 recommended).
2. Save the script as `main.py`.
3. Run the program:

```bash
python main.py
```

---

## 💡 How It Works

* When the program starts, it loads notes from `notes.csv` (if it exists).
* Users interact with a menu-driven interface.
* Each operation updates the in-memory list and saves it back to the CSV file.

---

## 📸 Example Output

```
My Notebook
1. Create note.
2. Vieww all note
3. Update a note
4. Delete a note
Enter your choice: 1

Create a note
Enter a title: Rose
Enter content: Rose is red
Note successfully created

My Notebook
1. Create note.
2. Vieww all note
3. Update a note
4. Delete a note
Enter your choice: 1

Create a note
Enter a title: The car
Enter content: The car is BMW
Note successfully created

My Notebook
1. Create note.
2. Vieww all note
3. Update a note
4. Delete a note
Enter your choice: 2

View all note
Index num: 1
Date/Time: 2026-05-02 18:04:06.750371
Title: Rose
Title: Rose is red
__________________________________________

Index num: 2
Date/Time: 2026-05-02 18:04:36.010642
Title: The car
Title: The car is BMW
__________________________________________

My Notebook
1. Create note.
2. Vieww all note
3. Update a note
4. Delete a note
Enter your choice: 3

Update a note
Enter the index number: 2
Note not found
Index num: 2
Date/Time: 2026-05-02 18:04:36.010642
Title: The car
Title: The car is BMW
-------------------------------------

Write the updated content: BMW and Toyota 
Note updated successfully!

My Notebook
1. Create note.
2. Vieww all note
3. Update a note
4. Delete a note
Enter your choice: 2

View all note
Index num: 1
Date/Time: 2026-05-02 18:04:06.750371
Title: Rose
Title: Rose is red
__________________________________________

Index num: 2
Date/Time: 2026-05-02 18:04:36.010642
Title: The car
Title: BMW and Toyota
__________________________________________

My Notebook
1. Create note.
2. Vieww all note
3. Update a note
4. Delete a note
Enter your choice: 4

Delete a note
Enter the index number: 1
Note successfully deleted

My Notebook
1. Create note.
2. Vieww all note
3. Update a note
4. Delete a note
Enter your choice: 2

View all note
Index num: 1
Date/Time: 2026-05-02 18:04:36.010642
Title: The car
Title: BMW and Toyota
__________________________________________
```
