import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",       # your MySQL username
    password="password",       # your MySQL password
    database="student_db"
)
cursor = con.cursor()

# Function to save student data
def register_student():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    course = entry_course.get()

    if name == "" or email == "" or age == "" or course == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        try:
            cursor.execute(
                "INSERT INTO students (name, email, age, course) VALUES (%s, %s, %s, %s)",
                (name, email, age, course)
            )
            con.commit()
            messagebox.showinfo("Success", "Student Registered Successfully!")
            entry_name.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_age.delete(0, tk.END)
            entry_course.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

# Tkinter Form
root = tk.Tk()
root.title("Student Registration Form")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

tk.Label(root, text="Course").grid(row=3, column=0, padx=10, pady=5)
entry_course = tk.Entry(root)
entry_course.grid(row=3, column=1)

tk.Button(root, text="Register", command=register_student).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()