from school_programs import SchoolPrograms

class ProgramService:
    def __init__(self):
        self.programs = [
            SchoolPrograms("Computer Science"),
            SchoolPrograms("Mathematics"),
            SchoolPrograms("Physics"),
            SchoolPrograms("Chemistry"),
            SchoolPrograms("Biology"),
            SchoolPrograms("Engineering"),
            SchoolPrograms("Business Administration"),
            SchoolPrograms("Psychology")
        ]

    def get_all_programs(self):
        return self.programs