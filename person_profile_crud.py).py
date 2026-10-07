import tkinter as tk
from tkinter import ttk,messagebox
import sqlite3

root = tk.Tk()
root.title("Student Information System")
root.geometry("700x500")

title_label = tk.Label(
    root,
    text = "Student Information System",
    font = ('Arial',18, "bold")
    )

title_label.pack(pady = 10)

input_frame = tk.Frame(root)
input_frame.pack(pady = 10)

tk.Label(
    input_frame,
    text = "Name:"
    ).grid(row = 0, column = 0, padx = 5, pady = 5)

name_entry = tk.Entry(input_frame,width=30)
name_entry.grid(row = 0,column = 1,padx = 5,pady = 5)

tk.Label(
    input_frame,
    text = "Course:"
    ).grid(row = 2, column = 0, padx = 5, pady = 5)

course_entry = tk.Entry(input_frame,width=30)
course_entry.grid(row = 2,column = 1,padx = 5,pady = 5)

button_frame =tk.Frame(root)
button_frame.pack(pady = 10)

tk.Button(
    button_frame,
    text = "Add",
    width = 10,
    command = "add_student"
    ).grid(row = 0, column = 0, padx = 5)

tk.Button(
    button_frame,
    text = "Update",
    width = 10,
    command = "update_student"
    ).grid(row = 0, column = 1, padx = 5)

tk.Button(
    button_frame,
    text = "Delete",
    width = 10,
    command = "delete_student"
    ).grid(row = 0, column = 2, padx = 5)

tk.Button(
    button_frame,
    text = "Clear",
    width = 10,
    command = "clear_student"
    ).grid(row = 0, column = 3, padx = 5)

tree = ttk.Treeview(
    root,
    columns =("ID","Name","Age","Course"),
    show = "headings"
    )

tree.heading("ID",text = "ID")
tree.heading("Name",text = "Name")
tree.heading("Age",text = "Age")
tree.heading("Course",text = "Course")

tree.column("ID", width = 50)
tree.column("Name", width = 200)
tree.column("Age", width = 80)
tree.column("Course", width = 200)


tree.pack(
    fil = "both",
    expand = True,
    padx = 10,
    pady = 10,
    )

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXIST Student(
id Integer,Primary Key,Auto Increment
name: Text,Not Null
email: Text,Not Null
phone: Text,Not Null
city: Text,Not Null
age: Integer,Not Null

)
""")

conn.commit()

def add_student():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    city = city_entry.get()
    age = age_entry.get()
    
    if name == "" or age == "" or course == "":
        messagebox.showwarning(
            "Warning"
            "Please fill in all fields."
            )
        return

    try:
        age = int (age)
    except ValueError:
            messagebox.showerror(
                "Error"
                "Age must be a number"
                )
            return

    cursor.execute(
            "INSERT INTO Students (name,email,phone,city,age) VALUES (?,?,?,?,?)",
            (name,email,phone,city,age)
        )

    conn.commit()

    messagebox.showinfo(
            "Success"
            "Student added successfully."
        )

    clear_fields()
    display_students()

def display_students():
    for item in tree.get_children():
        tree.delete(item)

    cunsor.execute("SELECT * FROM Students")
    student = cunsor.fetchall()

    for student in students:
            tree.insert("", tk.END, values=student)
                
            

        










    
