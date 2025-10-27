using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;

namespace BlazorApp1.Models
{
    public class StudentService
    {
        private readonly List<Student> students;

        public StudentService()
        {
            students =
            [
                new(1, "John", "Doe", new DateTime(2000, 1, 15), "Male", 3.5m, 4, 5, "Computer Science"),
                new(2, "Jane", "Smith", new DateTime(1999, 6, 30), "Female", 3.8m, 6, 4, "Mathematics"),
                new(3, "Alice", "Johnson", new DateTime(2001, 3, 22), "Female", 3.2m, 2, 3, "Physics"),
                new(4, "Bob", "Brown", new DateTime(2000, 11, 5), "Male", 3.6m, 5, 5, "Chemistry")
            ];
        }

        private int GenerateId()
        {
            int newId = 1;
            while (students.Any(s => s.Id == newId))
            {
                newId++;
            }
            return newId;
        }

        public void EnrollStudent(string firstName, string lastName, DateTime dateOfBirth, string gender, decimal gpa, int currentSemester, int numberOfCourses, string programEnrolled)
        {
            int newId = GenerateId();
            Student newStudent = new Student(newId, firstName, lastName, dateOfBirth, gender, gpa, currentSemester, numberOfCourses, programEnrolled);
            students.Add(newStudent);
        }

        public List<Student> GetAllStudents()
        {
            return students;
        }

        public Student GetStudentById(int id)
        {
            Student? student = students.FirstOrDefault(s => s.Id == id) ??
            throw new Exception($"Student with ID {id} not found.");
            return student;
        }

        public void ModifyStudent(int id, string firstName, string lastName, DateTime dateOfBirth, string gender, decimal gpa, int currentSemester, int numberOfCourses, string programEnrolled)
        {
            Student student = GetStudentById(id);
            if (student != null)
            {
                student.FirstName = firstName;
                student.LastName = lastName;
                student.DateOfBirth = dateOfBirth;
                student.Gender = gender;
                student.GPA = gpa;
                student.CurrentSemester = currentSemester;
                student.NumberOfCourses = numberOfCourses;
                student.ProgramEnrolled = programEnrolled;
            }
        }

        public void DeleteStudent(int id)
        {
            Student student = GetStudentById(id);
            if (student != null)
            {
                students.Remove(student);
            }
        }
    };
}   
