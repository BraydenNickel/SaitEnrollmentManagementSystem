from datetime import date

#Exception for validation errors
class ValidationError(Exception):
    pass

class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, gender, gpa, current_semester, number_of_courses, program_enrolled):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.gpa = gpa
        self.current_semester = current_semester
        self.number_of_courses = number_of_courses
        self.program_enrolled = program_enrolled

    def validate(self):
        #replicating c# [Required] and [Range] validations.
        if not self.first_name:
            raise ValidationError("First name is required.")
        if not self.last_name:
            raise ValidationError("Last name is required")
        if not isinstance(self.date_of_birth, date):
            raise ValidationError("Date of birth must be a valid date")
        if not self.gender:
            raise ValidationError("Gender is required")
        if not (0.0 <= self.gpa <= 4.0):
            raise ValidationError("GPA must be between 0.0 and 4.0")
        if not (1 <= self.current_semester <= 12):
            raise ValidationError("Current Semester must be between 1 and 12")
        if not(1 <= self.number_of_courses <= 8):
            raise ValidationError("Number of courses must be between 1 and 8")
        if not self.program_enrolled:
            raise ValidationError("Program enrolled is required")
        

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_id(self):
        return self.id
    