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
        for F in (LoginPage, VeiwListingPage, CheckOutPage, ListingPage, AdminPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the first page
        self.show_frame(LoginPage)

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

        self.users = get_users()  # Store the full data
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox.pack(padx=10, pady=10)

        # Show only usernames in the listbox
        for user in self.users:
            self.listbox.insert(tk.END, user[1])  # assuming column 1 = username

        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        tk.Button(self, text="Go to viewing page",
                  command=lambda: controller.show_frame(VeiwListingPage)).pack(pady=10)
        self.cartButton = tk.Button(
            self,
            text="Go to Cart",
            command=lambda: controller.show_frame(CheckOutPage)
        )
        self.cartButton.pack(pady=10)
        self.manageListingsButton = tk.Button(
            self,
            text="Go to manage listing",
            command=lambda: controller.show_frame(ListingPage)
        )
        self.manageListingsButton.pack(pady=10)
        self.adminManageButton = tk.Button(
            self,
            text="Go to admin page",
            command=lambda: controller.show_frame(AdminPage)
        )
        self.adminManageButton.pack(pady=10)
        self.toggle()

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        if not selected_index:
            self.toggle()
            return
        
        index = selected_index[0]
        selected_row = self.users[index]
        print("Selected row:", selected_row)

        # Store values
        global you
        you = list(selected_row[:3])  # first 3 columns
        print("Saved to you:", you)

        # Clear cart
        clear_cart()

        self.toggle()

    def toggle(self):
        global you
        try:
            role = you[2]
            
            self.cartButton.pack()#show because user is signned in
            
            if(role == "Seller" or role == "Admin"):
                self.manageListingsButton.pack()
                if(role == "Admin"):
                    self.adminManageButton.pack()
                else:
                    self.adminManageButton.pack_forget()
            else:
                self.manageListingsButton.pack_forget()#hide if user does not have a standard role
                self.adminManageButton.pack_forget()
        except:
            self.cartButton.pack_forget()#hide if user not signned in
            self.manageListingsButton.pack_forget()
            self.adminManageButton.pack_forget()

    def refresh(self):
        """Called every time the frame is shown."""

        # Clear old items
        self.listbox.delete(0, tk.END)

        for user in self.users:
            self.listbox.insert(tk.END, user[1])  # assuming column 1 = username

        self.listbox.bind("<<ListboxSelect>>", self.on_select)


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Login Page", font=("Arial", 18)).pack(pady=20)
        tk.Label(self, text="Select an account to use it", font=("Arial", 18)).pack(pady=20)

        self.users = get_users()  # Store the full data
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox.pack(padx=10, pady=10)

        # Show only usernames in the listbox
        for user in self.users:
            self.listbox.insert(tk.END, user[1])  # assuming column 1 = username

        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        tk.Button(self, text="Go to viewing page",
                  command=lambda: controller.show_frame(VeiwListingPage)).pack(pady=10)
        self.cartButton = tk.Button(
            self,
            text="Go to Cart",
            command=lambda: controller.show_frame(CheckOutPage)
        )
        self.cartButton.pack(pady=10)
        self.manageListingsButton = tk.Button(
            self,
            text="Go to manage listing",
            command=lambda: controller.show_frame(ListingPage)
        )
        self.manageListingsButton.pack(pady=10)
        self.adminManageButton = tk.Button(
            self,
            text="Go to admin page",
            command=lambda: controller.show_frame(AdminPage)
        )
        self.adminManageButton.pack(pady=10)
        self.toggle()

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        if not selected_index:
            self.toggle()
            return
        
        index = selected_index[0]
        selected_row = self.users[index]
        print("Selected row:", selected_row)

        # Store values
        global you
        you = list(selected_row[:3])  # first 3 columns
        print("Saved to you:", you)

        # Clear cart
        clear_cart()

        self.toggle()

    def toggle(self):
        global you
        try:
            role = you[2]
            
            self.cartButton.pack()#show because user is signned in
            
            if(role == "Seller" or role == "Admin"):
                self.manageListingsButton.pack()
                if(role == "Admin"):
                    self.adminManageButton.pack()
                else:
                    self.adminManageButton.pack_forget()
            else:
                self.manageListingsButton.pack_forget()#hide if user does not have a standard role
                self.adminManageButton.pack_forget()
        except:
            self.cartButton.pack_forget()#hide if user not signned in
            self.manageListingsButton.pack_forget()
            self.adminManageButton.pack_forget()

    def refresh(self):
        """Called every time the frame is shown."""

        # Clear old items
        self.listbox.delete(0, tk.END)

        for user in self.users:
            self.listbox.insert(tk.END, user[1])  # assuming column 1 = username

        self.listbox.bind("<<ListboxSelect>>", self.on_select)


if __name__ == "__main__":
    create_tables()

    if(get_users() == []):
        add_default_users()
        add_custom_users("Admin2","Admin")
    if(get_listing() == []):
        add_default_listings()

    app = App()
    app.mainloop()
