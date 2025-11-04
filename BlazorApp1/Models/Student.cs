using System.ComponentModel.DataAnnotations;
public class Student
{
    public int Id { get; set; }

    [Required]
    public string FirstName { get; set; }

    [Required]
    public string LastName { get; set; }

    [Required]
    public DateTime DateOfBirth { get; set; }

    [Required]
    public string Gender { get; set; }

    [Range(0.0, 4.0, ErrorMessage = "GPA must be between 0.0 and 4.0")]
    public decimal GPA { get; set; }

    [Range(1, 12, ErrorMessage = "Current Semester must be between 1 and 12")]
    public int CurrentSemester { get; set; }

    [Range(1, 8, ErrorMessage = "Number of Courses must be between 1 and 8")]
    public int NumberOfCourses { get; set; }

    [Required]
    public string ProgramEnrolled { get; set; }

    public Student() { }

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
