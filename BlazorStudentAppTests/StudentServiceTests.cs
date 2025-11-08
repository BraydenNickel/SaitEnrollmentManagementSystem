using System;
using Xunit;
using BlazorApp1.Models;
using System.Linq;
using System.ComponentModel.DataAnnotations;

namespace BlazorStudentAppTests
{
    public class StudentServiceTests
    {
        private readonly StudentService _studentService;

        public StudentServiceTests()
        {
            _studentService = new StudentService();
        }

        public void Dispose()
        {
            _studentService.GetAllStudents().Clear();
        }

        [Fact]
        public void TC01_EnrollStudent_ShouldAddNewStudent()
        {
            // Arrange
            int initialCount = _studentService.GetAllStudents().Count;

            // Act
            _studentService.EnrollStudent("Test", "User", new DateTime(2002, 5, 20), "Non-binary", 3.0m, 3, 4, "Engineering");
            int newCount = _studentService.GetAllStudents().Count;

            // Assert
            Assert.Equal(initialCount + 1, newCount);
        }

        [Fact]
        public void TC02_GetStudentById_ShouldReturnCorrectStudent()
        {
            // Arrange
            var student = _studentService.GetAllStudents().First();

            // Act
            var fetchedStudent = _studentService.GetStudentById(student.Id);

            // Assert
            Assert.Equal(student.Id, fetchedStudent.Id);
            Assert.Equal(student.FirstName, fetchedStudent.FirstName);
        }
        [Fact]
        public void TC03_ModifyStudent_ShouldUpdateStudentDetails()
        {
            // Arrange
            var student = _studentService.GetAllStudents().First();
            string newFirstName = "UpdatedName";

            // Act
            _studentService.ModifyStudent(student.Id, newFirstName, student.LastName, student.DateOfBirth, student.Gender, student.GPA, student.CurrentSemester, student.NumberOfCourses, student.ProgramEnrolled);
            var updatedStudent = _studentService.GetStudentById(student.Id);
            // Assert
            Assert.Equal(newFirstName, updatedStudent.FirstName);
        }

        [Fact]
        public void TC04_GetStudentById_InvalidId_ShouldThrowException()
        {
            // Arrange
            int invalidId = -1;

            // Act & Assert
            var exception = Assert.Throws<Exception>(() => _studentService.GetStudentById(invalidId));
            Assert.Equal($"Student with ID {invalidId} not found.", exception.Message);
        }

        [Fact]
        public void TC05_DeleteStudent_ShouldRemoveStudent()
        {
            // Arrange
            var student = _studentService.GetAllStudents().First();
            int initialCount = _studentService.GetAllStudents().Count;

            // Act
            _studentService.DeleteStudent(student.Id);
            int newCount = _studentService.GetAllStudents().Count;

            // Assert
            Assert.Equal(initialCount - 1, newCount);
        }

        [Fact]
        public void TC06_SearchStudentsByName_ShouldReturnMatchingStudents()
        {
            // Arrange
            string searchName = "Jane";

            // Act
            var results = _studentService.SearchStudentsByName(searchName);

            // Assert
            Assert.All(results, s => Assert.Contains(searchName, s.GetFullName(), StringComparison.OrdinalIgnoreCase));
        }

        [Fact]
        public void TC07_SearchStudentsByName_NoMatches_ShouldReturnEmptyList()
        {
            // Arrange
            string searchName = "NonExistentName";

            // Act
            var results = _studentService.SearchStudentsByName(searchName);

            // Assert
            Assert.Empty(results);
        }

        [Fact]
        public void TC08_EnrollStudent_InvalidGPA_ShouldThrowValidationException()
        {
            // Arrange
            decimal invalidGpa = 5.0m; // GPA should be between 0.0 and 4.0

            // Act & Assert
            var exception = Assert.Throws<ValidationException>(() =>
                _studentService.EnrollStudent("Invalid", "GPA", new DateTime(2000, 1, 1), "Male", invalidGpa, 1, 3, "Computer Science"));
            Assert.Equal("GPA must be between 0.0 and 4.0", exception.Message);
        }

        [Fact]
        public void TC09_EnrollStudent_InvalidSemester_ShouldThrowValidationException()
        {
            // Arrange
            int invalidSemester = 15; // Semester should be between 1 and 12

            // Act & Assert
            var exception = Assert.Throws<ValidationException>(() =>
                _studentService.EnrollStudent("Invalid", "Semester", new DateTime(2000, 1, 1), "Female", 3.0m, invalidSemester, 3, "Mathematics"));
            Assert.Equal("Current Semester must be between 1 and 12", exception.Message);
        }
        [Fact]
        public void TC10_EnrollStudent_InvalidNumberOfCourses_ShouldThrowValidationException()
        {
            // Arrange
            int invalidNumberOfCourses = 10; // Number of courses should be between 1 and 8

            // Act & Assert
            var exception = Assert.Throws<ValidationException>(() =>
                _studentService.EnrollStudent("Invalid", "Courses", new DateTime(2000, 1, 1), "Non-binary", 3.0m, 2, invalidNumberOfCourses, "Physics"));
            Assert.Equal("Number of Courses must be between 1 and 8", exception.Message);
        }

        [Fact]
        public void TC11_ModifyStudent_InvalidGPA_ShouldThrowValidationException()
        {
            // Arrange
            var student = _studentService.GetAllStudents().First();
            decimal invalidGpa = -1.0m; // GPA should be between 0.0 and 4.0

            // Act & Assert
            var exception = Assert.Throws<ValidationException>(() =>
                _studentService.ModifyStudent(student.Id, student.FirstName, student.LastName, student.DateOfBirth, student.Gender, invalidGpa, student.CurrentSemester, student.NumberOfCourses, student.ProgramEnrolled));
            Assert.Equal("GPA must be between 0.0 and 4.0", exception.Message);
        }

        [Fact]
        public void TC12_ModifyStudent_InvalidSemester_ShouldThrowValidationException()
        {
            // Arrange
            var student = _studentService.GetAllStudents().First();
            int invalidSemester = 0; // Semester should be between 1 and 12

            // Act & Assert
            var exception = Assert.Throws<ValidationException>(() =>
                _studentService.ModifyStudent(student.Id, student.FirstName, student.LastName, student.DateOfBirth, student.Gender, student.GPA, invalidSemester, student.NumberOfCourses, student.ProgramEnrolled));
            Assert.Equal("Current Semester must be between 1 and 12", exception.Message);
        }
        [Fact]
        public void TC13_ModifyStudent_InvalidNumberOfCourses_ShouldThrowValidationException()
        {
            // Arrange
            var student = _studentService.GetAllStudents().First();
            int invalidNumberOfCourses = 9; // Number of courses should be between 1 and 8

            // Act & Assert
            var exception = Assert.Throws<ValidationException>(() =>
                _studentService.ModifyStudent(student.Id, student.FirstName, student.LastName, student.DateOfBirth, student.Gender, student.GPA, student.CurrentSemester, invalidNumberOfCourses, student.ProgramEnrolled));
            Assert.Equal("Number of Courses must be between 1 and 8", exception.Message);
        }

        [Fact]
        public void TC14_DeleteStudent_InvalidId_ShouldThrowException()
        {
            // Arrange
            int invalidId = 9999;

            // Act & Assert
            var exception = Assert.Throws<Exception>(() => _studentService.DeleteStudent(invalidId));
            Assert.Equal($"Student with ID {invalidId} not found.", exception.Message);
        }

        [Fact]
        public void TC15_GetAllStudents_ShouldReturnAllEnrolledStudents()
        {
            // Arrange
            int expectedCount = _studentService.GetAllStudents().Count;

            // Act
            var allStudents = _studentService.GetAllStudents();

            // Assert
            Assert.Equal(expectedCount, allStudents.Count);
        }

        [Fact]
        public void TC16_EnrollStudent_DuplicateId_ShouldGenerateUniqueId()
        {
            // Arrange
            var existingStudent = _studentService.GetAllStudents().First();
            int existingId = existingStudent.Id;

            // Act
            _studentService.EnrollStudent("Duplicate", "ID", new DateTime(2001, 3, 15), "Female", 3.5m, 2, 4, "Biology");
            var newStudent = _studentService.GetAllStudents().Last();
            // Assert
            Assert.NotEqual(existingId, newStudent.Id);
        }

        [Fact]
        public void TC17_LoadEmptyStudentList_ShouldReturnEmptyList()
        {
            // Arrange
            var emptyStudentService = new StudentService();
            // Clear existing students
            foreach (var student in emptyStudentService.GetAllStudents().ToList())
            {
                emptyStudentService.DeleteStudent(student.Id);
            }

            // Act
            var allStudents = emptyStudentService.GetAllStudents();

            // Assert
            Assert.Empty(allStudents);
        }

        [Fact]
        public void TC18_Enroll100Students_ShouldHandleLargeNumberOfEntries()
        {
            // Arrange
            var largeStudentService = new StudentService();
            // Clear existing students
            foreach (var student in largeStudentService.GetAllStudents().ToList())
            {
                largeStudentService.DeleteStudent(student.Id);
            }

            // Act
            for (int i = 1; i <= 100; i++)
            {
                largeStudentService.EnrollStudent($"FirstName{i}", $"LastName{i}", new DateTime(2000, 1, 1).AddDays(i), "Male", 3.0m, 2, 4, "Engineering");
            }
            var allStudents = largeStudentService.GetAllStudents();
            // Assert
            Assert.Equal(100, allStudents.Count);
        }
    }
}