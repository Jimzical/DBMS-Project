import streamlit as st
from components.helper_components import ColoredHeader, make_connection
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from st_pages import add_page_title, add_indentation

def get_instructors_data(conn):
    # TODO: use sql to get the instructors data

    # sample
    # instructors_df = conn.query("select * from instructors")

    # temp
    # create a sample dataframe with data

    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")

    cursor.execute("SELECT * FROM instructor")
    records = cursor.fetchall()

    print(records)
    instructors_df = pd.DataFrame(records)
    instructors_df.columns = ['ID', 'Name', 'Department', 'Email']
    
    # instructors_df = pd.DataFrame(
    #     {
    #         "instructor_id": [1, 2, 3, 4, 5],
    #         "instructor_name": [
    #             "Dr. A",
    #             "Dr. B",
    #             "Dr. C",
    #             "Dr. D",
    #             "Dr. E",
    #         ],
    #         "instructor_email": [
    #             "uni_A@gmail.com",
    #             "uni_B@gmail.com",
    #             "uni_C@gmail.com",
    #             "uni_D@gmail.com",
    #             "uni_E@gmail.com"
    #         ]
    #     }
    # )

    return instructors_df



    

def instructors_main_func():
    # ADDING CONNECTION HERE
    # sample
    # conn = st.experimental_connection("sql")

    # temp
    conn = make_connection()

    instructors_df = get_instructors_data(conn)

    df = dataframe_explorer(instructors_df)
    st.dataframe(df)

if __name__ == "__main__":
    add_page_title()
    instructors_main_func()

    
