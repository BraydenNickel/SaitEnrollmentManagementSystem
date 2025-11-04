import sqlite3
import tkinter as tk
import datetime

class students:
    def __init__(self, ID, FirstName, LastName, 
                 DateOfBirth, Gender, 
                 GPA, CurrentSemester, 
                 NumberOfCourses, ProgramEnrolled):
        self.Id = ID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Gender = Gender
        self.GPA = GPA
        self.CurrentSemester = CurrentSemester
        self.NumberOfCourses = NumberOfCourses
        self.ProgramEnrolled = ProgramEnrolled

    def get_name(self):
        return self.FirstName + self.LastName

class StudentService:
    def __init__(self):
        self.students = [
                students(1, "John", "Doe", datetime.datetime(2000, 1, 15), "Male", "3.5m", 4, 5, "Computer Science"),
                students(2, "Jane", "Smith", datetime.datetime(1999, 6, 30), "Female", "3.8m", 6, 4, "Mathematics"),
                students(3, "Alice", "Johnson", datetime.datetime(2001, 3, 22), "Female", "3.2m", 2, 3, "Physics"),
                students(4, "Bob", "Brown", datetime.datetime(2000, 11, 5), "Male", "3.6m", 5, 5, "Chemistry")
            ]
    
    def GetAllStudents(self):
        return self.students

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Enrollment System")
        self.geometry("1500x1600")

        # Container for all pages
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary to hold pages
        self.frames = {}

        # Add pages to the container
        for F in (MainPage,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the first page
        self.show_frame(MainPage)

    def show_frame(self, page_class):
        """Raise the selected page to the top"""
        frame = self.frames[page_class]
        frame.tkraise()

        # Call refresh/update if it exists, to update page, before showing
        if hasattr(frame, "refresh"):
            frame.refresh()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Login Page", font=("Arial", 18)).pack(pady=20)
        tk.Label(self, text="Select an account to use it", font=("Arial", 18)).pack(pady=20)

        self.studentService = StudentService()
        self.students = self.studentService.GetAllStudents()  # Store the full data
        self.selectedStudent = None
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox.pack(padx=10, pady=10)

        # Show only usernames in the listbox
        for student in self.students:
            self.listbox.insert(tk.END, student.get_name())

        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.toggle()

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        if not selected_index:
            self.toggle()
            return
        
        index = selected_index[0]
        selected_row = self.students[index]
        print("Selected row:", selected_row)

        # Store values
        self.selectedStudent = list(selected_row[:3])  # first 3 columns
        print("Selected student:", self.selectedStudent)

        self.toggle()

    def toggle(self):
        global you

    def refresh(self):
        """Called every time the frame is shown."""

        # Clear old items
        self.listbox.delete(0, tk.END)

        self.students = self.studentService.GetAllStudents()  # Store the full data
        for student in self.students:
            self.listbox.insert(tk.END, student.get_name())

        self.listbox.bind("<<ListboxSelect>>", self.on_select)

if __name__ == "__main__":
    app = App()
    app.mainloop()
