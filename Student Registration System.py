import tkinter as tk
from tkinter import messagebox
#classes
class Person:
    def __init__(self, name, age, id, email):
        self.name = name
        self.age = age
        self.id = id
        self.email = email + '@dah.edu.sa'

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def set_age(self, new_age):
        self.age = new_age

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


    def display_info(self):
        return f"ID: {self.id} | Name: {self.name} | Age: {self.age} | Email: {self.email}"


class Student(Person):
    def __init__(self, name, age, id, email, gpa, major, gender):
        Person.__init__(self, name, age, id, email)
        self.gpa = gpa
        self.major = major
        self.gender = gender

    def get_gpa(self):
        return self.gpa

    def get_major(self):
        return self.major

    def get_gender(self):
        return self.gender

    def set_major(self, new_major):
        self.major = new_major

    def can_graduate(self):
        if self.gpa >= 2.0:
            return True
        else:
            return False

    def display_info(self):
        return f"Student {self.id} | {self.name} | Major: {self.major} | GPA: {self.gpa:.2f}"

# Additional class
class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def update_credits(self, new_credits):
        self.credits = new_credits

    def display_info(self):
        return f"{self.course_code} - {self.course_name} ({self.credits} credits)"

    def is_high_credit(self):
        if self.credits >= 3:
            return True
        else:
            return False

#exceptions
class NegativeGPAError(Exception):
    pass

class LowGPAError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class MissingDataError(Exception):
    pass

def student_infos(name, age, student_id, email, gpa, major, gender):
    try:
        if not name or not student_id or not email:
            raise MissingDataError("Name, ID, and Email are required.")

        if age <= 0:
            raise InvalidAgeError("Age must be positive.")

        if gpa < 0:
            raise NegativeGPAError("GPA can't be negative.")

        if gpa < 2.0:
            raise LowGPAError("GPA is below the university requirement.")

    except MissingDataError as m:
        print("Missing Data Error:", m)

    except InvalidAgeError as i:
        print("Invalid Age Error:", i)

    except NegativeGPAError as n:
        print("Invalid GPA Error:", n)
        return None

    except LowGPAError as l:
        print("Low GPA Error:", l)
    else:
        student = Student(name, age, student_id, email, gpa, major, gender)
        print("Student registered successfully.")
        return student
    finally:
        print("Student registration attempt is complete.")

#file I/O
def save_student_infos(student):
    try:
        with open("students.txt", "a") as file:
            file.write(student.name + "\n")
            file.write(str(student.age) + "\n")
            file.write(student.id + "\n")
            file.write(student.email + "\n")
            file.write(str(student.gpa) + "\n")
            file.write(student.major + "\n")
            file.write(student.gender + "\n")

        print("Student information saved successfully!")

    except FileNotFoundError:
        print("Error: The students file doesn't exist.")
    except Exception:
        print("Unexpected Error while saving the student information.")

def load_student_infos():
    try:
        with open("students.txt", "r") as file:
            print("Student Data:\n")

            for line in file:
                print(line.rstrip())

    except FileNotFoundError:
        print("Error: The students.txt file wasn't found.")

    except Exception:
        print("Unexpected Error while loading students file.")

def save_log(message):
    try:
        with open("log.txt", "a") as file:
            file.write(message + "\n")
    except Exception:
        print("Error writing log.")


class StudentRegistrationGUI:
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Student Registration System")
        self.mainWindow.geometry("900x500")

        form_frame = tk.LabelFrame(self.mainWindow, text="Student Information")
        form_frame.pack(padx=20, pady=15, fill="x")

        self.students = []

        tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Age").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.age_entry = tk.Entry(form_frame)
        self.age_entry.grid(row=0, column=3, padx=5, pady=5)
        tk.Label(form_frame, text="ID").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.id_entry = tk.Entry(form_frame)
        self.id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Email (username)").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="GPA").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.gpa_entry = tk.Entry(form_frame)
        self.gpa_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Major").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.major_entry = tk.Entry(form_frame)
        self.major_entry.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Gender").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.gender_entry = tk.Entry(form_frame)
        self.gender_entry.grid(row=3, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.mainWindow)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Add Student", command=self.add_student).pack(side="left", padx=15)
        tk.Button(button_frame, text="Show All", command=self.show_all).pack(side="left", padx=15)
        tk.Button(button_frame, text="Save", command=self.save_students).pack(side="left", padx=15)
        tk.Button(button_frame, text="Load", command=self.load_students).pack(side="left", padx=15)

        output_frame = tk.LabelFrame(self.mainWindow, text="Registered Students")
        output_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.output = tk.Text(output_frame, height=8)
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

    def add_student(self):
        try:
            student = student_infos(
                self.name_entry.get(),
                int(self.age_entry.get()),
                self.id_entry.get(),
                self.email_entry.get(),
                float(self.gpa_entry.get()),
                self.major_entry.get(),
                self.gender_entry.get()
            )

            if student:
                self.students.append(student)
                messagebox.showinfo("Success", "Student added successfully")

        except ValueError:
            messagebox.showerror("Error", "Age and GPA must be numbers")

    def show_all(self):
        self.output.delete("1.0", tk.END)
        for s in self.students:
            self.output.insert(tk.END, s.display_info() + "\n")

    def save_students(self):
        try:
            with open("students.txt", "w") as file:
                for s in self.students:
                    file.write(s.display_info() + "\n")
            messagebox.showinfo("Saved", "Students saved successfully")
        except Exception:
            messagebox.showerror("Error", "Could not save students")

    def load_students(self):
        try:
            self.output.delete("1.0", tk.END)
            with open("students.txt", "r") as file:
                for line in file:
                    self.output.insert(tk.END, line)
            messagebox.showinfo("Loaded", "Students loaded successfully")
        except FileNotFoundError:
            messagebox.showerror("Error", "students.txt not found")


if __name__ == "__main__":
    app = StudentRegistrationGUI()
    app.mainWindow.mainloop()
