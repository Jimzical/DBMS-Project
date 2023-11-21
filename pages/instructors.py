import streamlit as st
from components.helper_components import ColoredHeader, make_connection
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from st_pages import add_page_title, add_indentation

def get_instructors_data(conn):
    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")

    cursor.execute("SELECT * FROM instructor")
    records = cursor.fetchall()

    print(records)
    instructors_df = pd.DataFrame(records)
    instructors_df.columns = ['ID', 'Name', 'Department', 'Email']
    
    return instructors_df



    

def instructors_main_func():
    conn = make_connection()

    instructors_df = get_instructors_data(conn)

    df = dataframe_explorer(instructors_df)
    st.dataframe(df)

if __name__ == "__main__":
    add_page_title()
    instructors_main_func()

    
