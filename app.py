import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages
from components.helper_components import make_connection
# from pages.home import home_main_func
def pages():
    show_pages(
        [
        Page("pages/home.py", "Home", "🏠"),
        Page("pages/create.py", "Add Marks", "📝"),
        Page("pages/delete.py", "Delete Marks", "🗑️"),
        Section("Display", icon=":mag:"),
        Page("pages/electives.py", "Electives", "📚", in_section = True ),
        Page("pages/instructors.py", "Instructors", "👨‍🏫",in_section = True),
        Page("pages/students.py", "Students", "👨‍🎓",in_section = True),
        Page("pages/marks.py", "Marks", "📝",in_section = True)
        ]
    )

def create_tables():
    conn = make_connection()
    cursor = conn.cursor(buffered=True)

    cursor.execute("CREATE DATABASE IF NOT EXISTS student_marks")
    cursor.execute("USE student_marks")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student(
            ID varchar(20), 
            Name varchar(50), 
            email varchar(50), 
            DOB DATE, 
            PRIMARY KEY(ID)
        )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS instructor(
            ID int PRIMARY KEY, 
            Name varchar(30), 
            Dept varchar(30), 
            Email varchar(30)
        )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exam(
            ID varchar(20), 
            Student_ID varchar(20), 
            Marks int, 
            Date_Of_Exam DATE, 
            Course_ID varchar(20), 
            FOREIGN KEY(Student_ID) REFERENCES Student(ID)
        )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Course(
            ID varchar(50), 
            Name varchar(30), 
            Sem int, 
            Capacity int, 
            Classroom varchar(20),
            PRIMARY KEY(ID)
        )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Marks_Scored(
            Student_ID varchar(20), 
            Exam_ID varchar(20), 
            Marks_Obtained int, 
            FOREIGN KEY(Student_ID) REFERENCES Student(ID), 
            FOREIGN KEY(Exam_ID) REFERENCES Exam(ID)
        )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS elective(
            Student_ID varchar(20), 
            elective_1_ID varchar(50), 
            elective_2_ID varchar(50), 
            elective_3_ID varchar(50), 
            FOREIGN KEY(student_ID) REFERENCES Student(ID), 
            FOREIGN KEY(elective_1_ID) REFERENCES course(ID), 
            FOREIGN KEY(elective_2_ID) REFERENCES course(ID), 
            FOREIGN KEY(elective_3_ID) REFERENCES course(ID)
        )
        """)

    conn.commit()



def main():
    # home_main_func()
    create_tables()
    pages()

   


if __name__ == "__main__":
    main()