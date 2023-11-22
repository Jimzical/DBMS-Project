import streamlit as st
from components.helper_components import ColoredHeader, Notif,make_connection
from random import randint
import csv
import pandas as pd
from io import StringIO

def csv_template():
    with st.expander("How to Upload CSV"):
        st.write("1. Download the CSV Template")
        st.write("2. Fill the CSV Template with Required Details")
        st.write("3. Upload the CSV file")
        st.write("4. Click on Submit")

def template_files():
    with st.expander("Download CSV Template"):
        cl1 , cl2 , cl3 , cl4 = st.columns(4)
        with cl1:
            with open('sample/student.csv','r') as f:
                st.download_button(
                    label="For Student",
                    data=f,
                    file_name="student.csv",
                    key=randint(0,100000)
                )
        with cl2:
            with open('sample/instructor.csv','r') as f:
                st.download_button(
                    label="For Instructor",
                    data=f,
                    file_name="instructor.csv",
                    key=randint(0,100000)
                )
        with cl3:
            with open('sample/course.csv','r') as f:
                st.download_button(
                    label="For Course",
                    data=f,
                    file_name="course.csv",
                    key=randint(0,100000)
                )
        with cl4:
            with open('sample/elective.csv','r') as f:
                st.download_button(
                    label="For Elective",
                    data=f,
                    file_name="elective.csv",
                    key=randint(0,100000)
                )
        # with cl5:
        #     with open('sample/instructor.csv','r') as f:
        #         st.download_button(
        #             label="For instructor",
        #             data=f,
        #             file_name="instructor.csv",
        #             key=randint(0,100000)
        #         )
def adding_data(conn, file,table):
    data = []
    df = pd.read_csv(file)
    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")
    if table == "student":  
        for index,row in df.iterrows():
            data.append((row['ID'],row['Name'], row['Email'], row['DOB']))
        query = "INSERT INTO Student VALUES(%s, %s,%s,%s)"
        for i in data:
            cursor.execute(query,i)
    
    if table == "instructor":
        for index,row in df.iterrows():
            data.append((row['ID'],row['Name'], row['Dept'], row['Email']))
        query = "INSERT INTO Instructor VALUES(%s, %s,%s,%s)"
        for i in data:
            cursor.execute(query,i)
    
    if table =='elective':
        for index, row in df.iterrows():
            data.append((row['student_ID'], row['elective_1_ID'], row['elective_2_ID'], row['elective_3_ID']))
            
        query = "INSERT INTO elective VALUES(%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query,i)
    
    if table == 'course':
        for index, row in df.iterrows():
            data.append((row['ID'], row['Name'], row['Sem'], row['Capacity'], row['Classroom']))
        
        query = "INSERT INTO course VALUES(%s,%s,%s,%s,%s)"
        for i in data:
        
            cursor.execute(query,i)
        

    conn.commit()
    st.success(f"Records added to {table}")

    pass


def home_main_func():
    conn = make_connection()
    cursor = conn.cursor(buffered=True)

    ColoredHeader(
        label="Student Marks Management System",
        description="DBMS Project to manage Student Marks",
        color_name="gold",
        help="",
        description_help=""
    )


    csv_template()
    students = st.file_uploader("Upload Students CSV", type="csv")

    instructors = st.file_uploader("Upload Instructors CSV", type="csv")

    course = st.file_uploader("Upload Course CSV", type="csv")

    elective = st.file_uploader("Upload Elective CSV", type="csv")


    st.divider()
    template_files()

    submit= st.button("Submit")

    if submit:
        if students:
            st.write(students)
            adding_data(conn,students,"student")
        if instructors:
            st.write(instructors)
            adding_data(conn,instructors,"instructor")
        if elective:
            st.write(elective)
            adding_data(conn,elective,"elective")
        if course:
            st.write(course)
            adding_data(conn,course,"course")



if __name__ == "__main__":
    home_main_func()