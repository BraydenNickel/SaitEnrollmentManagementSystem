from datetime import date, datetime
from student_service import StudentService
from program_service import ProgramService

def display_student(student):
    print(f"""
ID: {student.id}
Name: {student.get_full_name()}
Date of Birth: {student.date_of_birth}
Gender: {student.gender}
GPA: {student.gpa}
Current Semester: {student.current_semester}
Number of Courses: {student.number_of_courses}
Program Enrolled: {student.program_enrolled}
""")
    
def list_students(service):
    students = service.get_all_students()
    if not students:
        print("No students found")
    else:
        for s in students:
            display_student(s)

def add_student(service, program_service):
    print("\n=== Enroll a New Student ===")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    dob_str = input("Date of Birth (YYYY-MM-DD): ").strip()
    gender = input("Gender: ").strip()
    gpa = float(input("GPA (0.0 - 4.0): ").strip())
    current_semester = int(input("Current Semester (1-12): ").strip())
    number_of_courses = int(input("Number of Courses (1-8): ").strip())

    print("\nAvailable Programs: ")
    for p in program_service.get_all_programs():
        print("-", p.name)
    program_enrolled = input("Program Enrolled: ").strip()

    try:
        date_of_birth = datetime.strptime(dob_str, "%Y-%m-%d").date()
        service.enroll_student(first_name, last_name, date_of_birth, gender, gpa, current_semester, number_of_courses, program_enrolled)
        print("Student enrolled successfully")
    except Exception as e:
        print(f"Error: {e}")
    
def modify_student(service):
    print("\n===Modify Existing Student ===")
    try:
        student_id = int(input("Enter Student ID: "))
        student = service.get_student_by_id(student_id)
        print("Leave field/s empty to keep current values.")
        first_name = input(f"First Name ({student.first_name}): ") or student.first_name
        last_name = input(f"Last Name ({student.last_name}): ") or student.last_name
        dob_str = input(f"Date of Birth ({student.date_of_birth}, YYYY-MM-DD): ") or str(student.date_of_birth)
        gender = input(f"Gender ({student.gender}): ") or student.gender
        gpa = input(f"GPA ({student.gpa}): ") or student.gpa
        current_semester = input(f"Semester ({student.current_semester}): ") or student.current_semester
        number_of_courses = input(f"Courses ({student.number_of_courses}): ") or student.number_of_courses
        program_enrolled = input(f"Program ({student.program_enrolled}): ") or student.program_enrolled

        date_of_birth = datetime.strptime(str(dob_str), "%Y-%m-%d").date()
        service.modify_student(student_id, first_name, last_name, date_of_birth, gender, float(gpa), int(current_semester), int(number_of_courses), program_enrolled)
        print("Student updated successfully")
    except Exception as e:
        print(f"Error: {e}")

def delete_student(service):
    try:
        student_id = int(input("\nEnter Student ID to delete: "))
        service.delete_student(student_id)
        print("Student deleted successfully")
    except Exception as e:
        print(f"Error: {e}")

def search_students(service):
    name = input("\nEnter name to search: ").strip()
    results = service.search_students_by_name(name)
    if results:
        print(f"\n Found{len(results)} student/s: ")
        for s in results:
            display_student(s)
    else:
        print("No matching students found.")

def main():
    student_service = StudentService()
    program_service = ProgramService()

    while True:
        print("""
========= Student Management System ========
1. View All Students
2. Enroll New Student
3. Modify Student
4. Delete Student
5. Search Student by Name              
6. Show Programs
0. Exit              
""")
        choice = input("Select an option: ").strip()

        if choice == "1":
            list_students(student_service)
        elif choice == "2":
            add_student(student_service, program_service)
        elif choice == "3":
            modify_student(student_service)
        elif choice == "4":
            delete_student(student_service)
        elif choice == "5":
            search_students(student_service)
        elif choice == "6":
            print("\nAvailable Programs: ")
            for p in program_service.get_all_programs():
                print("-", p.name)
        elif choice == "0":
            print("Thank you for using the Student Management System. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    