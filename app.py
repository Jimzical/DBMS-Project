import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages
from components.helper_components import make_connection
# from pages.home import home_main_func
def pages():
    show_pages(
        [
        Page("pages/home.py", "Home", "🏠"),
        Page("pages/add_marks.py", "Add Marks", "📝"),
        Page("pages/create.py","Update Marks", "📝"),
        Page("pages/delete.py", "Delete Items", "🗑️"),
        Page("pages/display.py","Display", icon=":mag:"),
        Page("pages/electives.py", "Electives", "📚", in_section = True ),
        Page("pages/instructors.py", "Instructors", "👨‍🏫",in_section = True),
        Page("pages/students.py", "Students", "👨‍🎓",in_section = True),
        Page("pages/marks.py", "Marks", "📝",in_section = True)
        ]
    )

def does_trigger_exist():
    conn = make_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")
    cursor.execute("SHOW TRIGGERS LIKE 'decrement_capacity_trigger'")
    conn.close()
    return cursor.fetchone() is not None


def set_trigger():
    print("ENTERED SET TRIGGER FUNCTION----")
    conn = make_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")
    trigger_exists = does_trigger_exist()
    try: 

        
        if not trigger_exists:
            print("Trigger does not exist, creating...")
            trigger_creation = '''
            

            CREATE TRIGGER decrement_capacity_trigger
            AFTER INSERT ON elective
            FOR EACH ROW
            BEGIN
                -- Decrease the capacity of the enrolled elective in the course table
                UPDATE course
                SET Capacity = Capacity - 1
                WHERE ID = NEW.elective_1_ID;

                UPDATE course
                SET Capacity = Capacity - 1
                WHERE ID = NEW.elective_2_ID;

                UPDATE course
                SET Capacity = Capacity - 1
                WHERE ID = NEW.elective_3_ID;
            END 

            
        '''
            cursor.execute(trigger_creation)
            
        print("Trigger succesfully created.")

        
    except:
        print("Trigger already exists")
    

    
    conn.commit()
    conn.close()
    return



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
            FOREIGN KEY(Student_ID) REFERENCES Student(ID) ON DELETE CASCADE
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
        CREATE TABLE IF NOT EXISTS elective(
            Student_ID varchar(20), 
            elective_1_ID varchar(50), 
            elective_2_ID varchar(50), 
            elective_3_ID varchar(50), 
            FOREIGN KEY(student_ID) REFERENCES Student(ID) ON DELETE CASCADE, 
            FOREIGN KEY(elective_1_ID) REFERENCES course(ID) ON DELETE CASCADE, 
            FOREIGN KEY(elective_2_ID) REFERENCES course(ID) ON DELETE CASCADE, 
            FOREIGN KEY(elective_3_ID) REFERENCES course(ID) ON DELETE CASCADE
        )
        """)

    conn.commit()
    conn.close()



def main():
    # home_main_func()
    create_tables()
    set_trigger()
    pages()

   


if __name__ == "__main__":
    main()