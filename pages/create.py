import streamlit as st
from components.helper_components import ColoredHeader, Notif

def heading():
    ColoredHeader(
        label="Add Marks 📝",
        description="Add marks for a student",
        color_name="gold",
        help="",
        description_help=""
    )

def get_student_name(conn):
    # TODO use sql to get student name
    # sample, replace with sql code to get student name
    # df = conn.query("select * from pet_owners")
    
    # temp for testing pursoses
    student_list = ["Student 1", "Student 2", "Student 3"]

    return student_list

def get_elective_subjects(conn,student_name):
    # TODO use sql to get elective subjects for student
    # sample, replace with sql code to get elective subjects for student
    # df = conn.query("select * from pet_owners")

    # temp for testing pursoses
    elective_subjects = ["Elective 1", "Elective 2"]

    return elective_subjects

def submit_marks(conn,student_name, elective_subject, isa1, isa2, esa):
    # TODO use sql to submit marks
    # sample, replace with sql code to submit marks
    # df = conn.query("select * from pet_owners")


    st.toast("Succesful ✅")
    Notif("success", 2.5, f"Name: {student_name} | Elective: {elective_subject} | ISA 1: {isa1} | ISA 2: {isa2} | ESA: {esa}")
    return True

def create_main_func():
    heading()

    
    # ADDING CONNECTION HERE
    # -----------------------------------------------------------------------------------------------------
    # for help
    # https://docs.streamlit.io/library/api-reference/connections/st.connections.sqlconnection
    # https://docs.streamlit.io/library/api-reference/connections/st.experimental_connection
    # conn = st.experimental_connection("sql")
    # for URL based crap
    # conn = st.experimental_connection(
    #     "local_db",
    #     type="sql",
    #     url="mysql://user:pass@localhost:3306/mydb"
    # )
    # -----------------------------------------------------------------------------------------------------


    # temp
    conn = 1
    
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