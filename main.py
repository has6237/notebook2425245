import datetime
import csv
import os
notes = []
file_name = "notes.csv"


def load_notes():
    #Loading the notes from csv file to notes=[]
    global notes
    notes = []
    if os.path.exists(file_name):
        with open(file_name, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                notes.append({
                    "title": row['title'],
                    "content": row['content'],
                    "date-time": row['date-time']
                })

def save_notes():
    #Saving a note to csv file
    with open(file_name, 'w', newline='') as file:
        fieldnames = ['title', 'content', 'date-time']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(notes)


def menu():
    print("My Notebook")
    print("1. Create note.")
    print("2. Vieww all note")
    print("3. Update a note")
    print("4. Delete a note")

    menuChoice = int(input("Enter your choice: "))

    if menuChoice == 1:
        create_note()
    elif menuChoice == 2:
        view_all()
    elif menuChoice == 3:
        update_note()
    elif menuChoice == 4:
        delete_note()
    else:
        print("Invalid choice!")
        menu()


def create_note():
    print("Create a note")
    title = input("Enter a title: ")
    content = input("Enter content: ")
    dateTime  = datetime.datetime.now()

    notes.append({
        "title": title,
        "content": content,
        "date-time": dateTime
    })

    print("Note successfully created")
    save_notes()
    menu()



def view_all():
    print("View all note")
    for i, note in enumerate(notes):
        print(f"Index num: {i+1}")
        print(f"Date/Time: {note['date-time']}")
        print(f"Title: {note['title']}")
        print(f"Title: {note['content']}")
        print("__________________________________________")
    menu()

def update_note():
    print("Update a note")
    index_num = int(input("Enter the index number: "))
    found = False
    for i, note in enumerate(notes):
        if i+1 == index_num:
         print(f"Index num: {i+1}")
         print(f"Date/Time: {note['date-time']}")
         print(f"Title: {note['title']}")
         print(f"Title: {note['content']}")
         print("-------------------------------------")

         updated_content = input("Write the updated content: ")
         note["content"] = updated_content
         save_notes()
         print("Note updated successfully!")
         found = True
         break
        if not found:
         print("Note not found")

    menu()


def delete_note():
    print("Delete a note")
    index_num = int(input("Enter the index number: "))
    found = False
    for i, note in enumerate(notes):
        if i+1 == index_num:
            notes.remove(note)
            save_notes()
            print("Note successfully deleted")
            found = True
            break
        if not found:
            print("Note not found")
    menu()

load_notes()
menu()