import streamlit as st
from components.helper_components import ColoredHeader, Notif,make_connection
import pandas as pd

def heading():
    ColoredHeader(
        label="Delete Items",
        color_name="gold",
        help="",
        description_help=""
    )

def deleting_mechanics():
    option = st.selectbox(
        label='''Choose What you want to delete''',
        options=['Student Table', 'Instructor Table', 'Course Table', 'Elective Table','Exam Table',"Delete All"]
    )

    if option == 'Student Table':
        st.write("Enter the ID of the student you want to delete")
        id = st.text_input(label="ID")
        if st.button(label="Delete"):
            conn = make_connection()
            cursor = conn.cursor(buffered=True)
            cursor.execute("USE student_marks")
            cursor.execute("DELETE FROM student WHERE ID = %s", (id,))
            conn.commit()
            conn.close()
            st.success("Deleted Successfully")
    elif option == 'Instructor Table':
        st.write("Enter the ID of the Instructor you want to delete")
        id = st.text_input(label="ID")
        if st.button(label="Delete"):
            conn = make_connection()
            cursor = conn.cursor(buffered=True)
            cursor.execute("USE student_marks")
            cursor.execute("DELETE FROM instructor WHERE ID = %s", (id,))
            conn.commit()
            conn.close()
            st.success("Deleted Successfully")
    elif option == 'Course Table':
        st.write("Enter the ID of the Course you want to delete")
        id = st.text_input(label="ID")
        if st.button(label="Delete"):
            conn = make_connection()
            cursor = conn.cursor(buffered=True)
            cursor.execute("USE student_marks")
            cursor.execute("DELETE FROM course WHERE ID = %s", (id,))
            conn.commit()
            conn.close()
            st.success("Deleted Successfully")
    elif option == 'Elective Table':
        st.write("Enter the ID of the Student whose Electives you want to delete")
        id = st.text_input(label="ID")
        if st.button(label="Delete"):
            conn = make_connection()
            cursor = conn.cursor(buffered=True)
            cursor.execute("USE student_marks")
            cursor.execute("DELETE FROM elective WHERE Student_ID = %s", (id,))
            conn.commit()
            conn.close()
            st.success("Deleted Successfully")
    elif option == 'Exam Table':
        st.write("Enter the ID of the Exam you want to delete")
        id = st.text_input(label="Student_ID")
        if st.button(label="Delete"):
            conn = make_connection()
            cursor = conn.cursor(buffered=True)
            cursor.execute("USE student_marks")
            cursor.execute("DELETE FROM exam WHERE Student_ID = %s", (id,))
            conn.commit()
            conn.close()
            st.success("Deleted Successfully")
    elif option == "Delete All":
        st.write("Are you sure you want to delete all the data?")
        if st.button(label="Yes"):
            conn = make_connection()
            cursor = conn.cursor(buffered=True)
            # drop student_marks
            cursor.execute("DROP DATABASE IF EXISTS student_marks")
            conn.commit()
            conn.close()
            st.success("Deleted Successfully")
        else:
            st.warning("Not Deleted")
def main():
    heading()
    deleting_mechanics()

if __name__ =="__main__":
    main()