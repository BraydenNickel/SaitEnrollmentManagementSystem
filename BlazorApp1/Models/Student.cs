using System;

public class Student
{
    public int Id { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public DateTime DateOfBirth { get; set; }
    public string Gender { get; set; }
    public decimal GPA { get; set; }
    public int CurrentSemester { get; set; }
    public int NumberOfCourses { get; set; }
    public string ProgramEnrolled { get; set; }

    public Student(int id, string firstName, string lastName, DateTime dateOfBirth, string gender, decimal gpa, int currentSemester, int numberOfCourses, string programEnrolled)
    {
        Id = id;
        FirstName = firstName;
        LastName = lastName;
        DateOfBirth = dateOfBirth;
        Gender = gender;
        GPA = gpa;
        CurrentSemester = currentSemester;
        NumberOfCourses = numberOfCourses;
        ProgramEnrolled = programEnrolled;
    }

    public string GetFullName()
    {
        return $"{FirstName} {LastName}";
    }

    public int GetID()
    {
        return Id;
    }

}
