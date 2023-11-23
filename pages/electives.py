import streamlit as st
from st_pages import add_page_title
from components.helper_components import ColoredHeader, make_connection
from streamlit_extras.dataframe_explorer import dataframe_explorer
from st_pages import add_page_title, add_indentation

import pandas as pd
def get_elective_date(conn):
    cursor = conn.cursor(buffered=True)
    cursor.execute("Use student_marks")
    cursor.execute("SELECT * FROM Course ")
    records = cursor.fetchall()
    columns = ['Course ID','Course Name','Semester', 'Capacity', 'Classroom']
    df = pd.DataFrame(records)
    df.columns = columns
    return df

def electives_main_func():
    conn = make_connection()

    elective_df = get_elective_date(conn)

    df = dataframe_explorer(elective_df)
    st.dataframe(df)
    


if __name__ == "__main__":
    add_page_title()
    electives_main_func()