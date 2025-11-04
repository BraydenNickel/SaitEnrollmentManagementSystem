using System.Collections.Generic;

namespace BlazorApp1.Models
{
    public class ProgramService
    {
        private readonly List<SchoolPrograms> programs;

        public ProgramService()
        {
            programs =
            [
                new SchoolPrograms("Computer Science"),
                new SchoolPrograms("Mathematics"),
                new SchoolPrograms("Physics"),
                new SchoolPrograms("Chemistry"),
                new SchoolPrograms("Biology"),
                new SchoolPrograms("Engineering"),
                new SchoolPrograms("Business Administration"),
                new SchoolPrograms("Psychology")
            ];
        }

        public List<SchoolPrograms> GetAllPrograms()
        {
            return programs;
        }
    }
}