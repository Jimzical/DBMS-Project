import streamlit as st
from components.helper_components import ColoredHeader, Notif
from random import randint

def csv_template():
    with st.expander("How to Upload CSV"):
        st.write("1. Download the csv template")
        st.write("2. Fill the csv template with instructor details")
        st.write("3. Upload the csv file")
        st.write("4. Click on submit")

def template_files():
    with st.expander("Download CSV Template"):
        cl1 , cl2 , cl3 = st.columns(3)
        with cl1:
            st.download_button(
                    label="for student",
                    data="for student",
                    key=randint(0,100000)
                )
        with cl2:
            st.download_button(
                    label="for instructor",
                    data="for instructor",
                    key=randint(0,100000)
                )
        with cl3:
            st.download_button(
                    label="for course",
                    data="for course",
                    key=randint(0,100000)
                )

def adding_data(conn, csv_file, table_name):
    # TODO: No clue how
    pass


def home_main_func():
    # TODO: Add home page content here like what its all about, how to use it, etc. 

    ColoredHeader(
        label="Student Marks Management System",
        description="DBMS Project to manage Student Marks",
        color_name="gold",
        help="",
        description_help=""
    )


    # TODO: Decide if we wanna do some crap like that. might need additional logic or we just just say fuck it and be like experimental feature so no constraint checking
    csv_template()
    students = st.file_uploader("Upload Students CSV", type="csv")

    instructors = st.file_uploader("Upload Instructors CSV", type="csv")

    courses = st.file_uploader("Upload Courses CSV", type="csv")

    st.divider()
    template_files()

    submit_student = st.button("Submit")

    if submit_student:
        st.experimental_rerun()
        
        adding_data()

if __name__ == "__main__":
    home_main_func()