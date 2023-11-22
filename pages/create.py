import streamlit as st
from components.helper_components import ColoredHeader, Notif,make_connection
import pandas as pd



def heading():
    ColoredHeader(
        label="Add Marks 📝",
        description="Add marks for a student",
        color_name="gold",
        help="",
        description_help=""
    )

def get_student_name(conn):

    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")
    
    cursor.execute("SELECT name FROM student")
    records = cursor.fetchall()
    student_list = []
    for i in records:
        student_list.append(i[0])

    return student_list

def get_elective_subjects(conn,student_name):
    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")
    cursor.execute("SELECT ID FROM student where Name = %s",(student_name,))
    id = cursor.fetchall()
    
    elective_list = []
    cursor.execute("SELECT * FROM elective WHERE student_ID = %s",id[0])
    records = cursor.fetchall()
    print(records)
    for i in records:
        elective_list.append(i[1])
        elective_list.append(i[2])
        elective_list.append(i[3])
    
    return elective_list

# def submit_marks(conn,student_name, elective_subject, isa1, isa2, esa):
#     cursor = conn.cursor(buffered=True)
#     cursor.execute("USE student_marks")
#     cursor.execute("SELECT ID from student where name = %s",(student_name,))
#     student_id = (cursor.fetchall())[0][0]
    
#     print(student_id)
  
#     # query = "INSERT INTO exam VALUES(%s, %s, %s, %s, %s)"
#     # values1 = ((elective_subject[:3] + "_" + "isa1"), student_id, isa1,20031210,elective_subject)
#     # values2 = ((elective_subject[:3] + "_" + "isa2"), student_id, isa2,20031210,elective_subject)
#     # values3 = ((elective_subject[:3] + "_" + "esa"), student_id, esa,20031210,elective_subject)
#     # cursor.execute(query,values1)
#     # cursor.execute(query,values2)
#     # cursor.execute(query,values3)

#     conn.commit()

#     st.toast("Succesful ✅")
#     Notif("success", 2.5, f"Name: {student_name} | Elective: {elective_subject} | ISA 1: {isa1} | ISA 2: {isa2} | ESA: {esa}")
#     return True

def submit_marks(conn, student_name, elective_subject, isa1, isa2, esa):
    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")
    cursor.execute("SELECT ID FROM student WHERE name = %s", (student_name,))
    student_id = cursor.fetchone()[0]

    # st.write(f'''
    #     student_name: {student_name}
    #     elective_subject: {elective_subject}
    #     isa1: {isa1}
    #     isa2: {isa2}
    #     esa: {esa}
    # ''')

    # Update existing rows
    query = (
        "UPDATE exam "
        "SET Marks = %d "
        "WHERE ID = %s AND Student_ID = %s AND Date_Of_Exam = %s AND Course_ID = %s"
    )

    # Update ISA 1
    val1 = (isa1, f"{elective_subject[:3]}_isa1", student_id, "2003-12-10", elective_subject)
    # # Update ISA 1
    # values1 = (isa1, f"{elective_subject[:3]}_isa1", student_id, "2003-12-10", elective_subject)
    # cursor.execute(query, values1)

    # # Update ISA 2
    # values2 = (isa2, f"{elective_subject[:3]}_isa2", student_id, "2003-12-10", elective_subject)
    # cursor.execute(query, values2)

    # # Update ESA
    # values3 = (esa, f"{elective_subject[:3]}_esa", student_id, "2003-12-10", elective_subject)
    # cursor.execute(query, values3)

    conn.commit()

    st.toast("Successful ✅")
    Notif("success", 2.5, f"Name: {student_name} | Elective: {elective_subject} | ISA 1: {isa1} | ISA 2: {isa2} | ESA: {esa}")
    return True

def create_main_func():
    heading()

    conn = make_connection()
    
    student_list = get_student_name(conn)
    selected_student = st.selectbox("Select Student", student_list)
    student_elective_list = get_elective_subjects(conn,selected_student)
    selected_elective = st.selectbox("Select Electives", student_elective_list)
    st.divider()
    
    st.subheader(selected_elective)
    col1, col2 , col3 = st.columns(3)
    with col1:
        isa1 = st.number_input("ISA 1", min_value=0, max_value=100)  
    with col2:
        isa2 = st.number_input("ISA 2", min_value=0, max_value=100)
    with col3:
        esa = st.number_input("ESA", min_value=0, max_value=100)

    submit = st.button("Submit")

    if submit:
        submit_marks(
            conn = conn,
            student_name = selected_student,
            elective_subject = selected_elective,
            isa1 = isa1,
            isa2 = isa2,
            esa = esa
        )

if __name__ == "__main__":
    create_main_func()