import streamlit as st
from components.helper_components import ColoredHeader,make_connection
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd
from st_pages import add_page_title, add_indentation

def get_students_data(conn):
    cursor = conn.cursor(buffered=True)

    cursor.execute("USE student_marks")

    cursor.execute("SELECT * from student")
    records = cursor.fetchall()
    students_df = pd.DataFrame(records)
    students_df.columns = ['ID', 'Name', 'Email', 'DOB']

    return students_df


def students_main_func():
    conn = make_connection()

    students_df = get_students_data(conn)

    df = dataframe_explorer(students_df)
    st.dataframe(df)


if __name__ == "__main__":
    add_page_title()
    students_main_func()
