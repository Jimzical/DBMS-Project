import streamlit as st
from components.helper_components import make_connection
import pandas as pd
import subprocess


def table_display():
    conn = make_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")
    
    table_name = st.selectbox('Select Table', ('Student', 'Instructor', 'Elective', 'Course', 'Exam'))
    
    # Fetch column names
    cursor.execute(f"DESCRIBE {table_name}")
    columns = [column[0] for column in cursor.fetchall()]

    # Fetch records
    cursor.callproc('DisplayTableRecords', (table_name,))
    for result in cursor.stored_results():
        records = result.fetchall()

        # Create DataFrame with column names
        df = pd.DataFrame(records, columns=columns)
        
        # Display DataFrame in Streamlit
        st.dataframe(df)

    
    # st.subheader("Student Table")
    # # convert to df
    # df = pd.read_sql("SELECT * FROM student", conn, index_col="ID")
    # st.dataframe(df)
    # st.divider()

    # st.subheader("Instructor Table")
    # df = pd.read_sql("SELECT * FROM instructor", conn, index_col="ID")
    # st.dataframe(df)
    # st.divider()

    # st.subheader("Course Table")
    # df = pd.read_sql("SELECT * FROM course", conn, index_col="ID")
    # st.dataframe(df)
    # st.divider()

    # st.subheader("Elective Table")
    # df = pd.read_sql("SELECT * FROM elective", conn, index_col="Student_ID")
    # st.dataframe(df)
    # st.divider()

    # st.subheader("Exam Table")
    # df = pd.read_sql("SELECT * FROM exam", conn, index_col="ID")
    # st.dataframe(df)
    # st.divider()

    # conn.close()
    

if __name__ == "__main__":
    with st.expander(label="Display Tables", expanded=True):
        table_display()