from datetime import date
from student import Student, ValidationError

class StudentService:
    def __init__(self):
        self.students = [
            Student(1, "John", "Doe", date(2000, 1, 15), "Male", 3.5, 4, 5, "Computer Science"),
            Student(2, "Jane", "Smith", date(1999, 6, 30), "Female", 3.8, 6, 4, "Mathematics"),
            Student(3, "Alice", "Johnson", date(2001, 3, 22), "Female", 3.2, 2, 3, "Physics"),
            Student(4, "Bob", "Brown", date(2000, 11, 5), "Male", 3.6, 5, 5, "Chemistry")
        ]

    def _generate_id(self):
        new_id = 1
        existing_ids = {student.id for student in self.students}
        while new_id in existing_ids:
            new_id += 1
        return new_id
    
    def enroll_student(self, first_name, last_name, date_of_birth, gender, gpa, current_semester, number_of_courses, program_enrolled):
        new_id = self._generate_id()
        new_student = Student(new_id, first_name, last_name, date_of_birth, gender, gpa, current_semester, number_of_courses, program_enrolled)
        self.students.append(new_student)

    def get_all_students(self):
        return self.students
    
    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        raise ValueError(f"Student with ID {student_id} not found.")
    
    def modify_student (self, student_id, first_name, last_name, date_of_birth, gender, gpa, current_semester, number_of_courses, program_enrolled):
        student = self.get_student_by_id(student_id)
        student.first_name = first_name
        student.last_name = last_name
        student.date_of_birth = date_of_birth
        student.gender = gender
        student.gpa = gpa
        student.current_semester = current_semester
        student.number_of_courses = number_of_courses
        student.program_enrolled = program_enrolled
        student.validate()

    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)
        self.students.remove(student)

    def search_students_by_name(self, name):
        return [s for s in self.students if name.lower() in s.get_full_name().lower()]
    
    def get_students_above_gpa(self, min_gpa):
        return [s for s in self.students if s.gpa >= min_gpa]
    
    def filter_students(self, filter_func):
        for student in self.students:
            if filter_func(student):
                yield student
