import streamlit as st
from components.helper_components import ColoredHeader
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd
def get_students_data(conn):
    # TODO: use sql to get the students data

    # sample
    # students_df = conn.query("select * from students")

    # temp
    # create a sample dataframe with data
    students_df = pd.DataFrame(
        {
            "student_id": [1, 2, 3, 4, 5],
            "student_name": [
                "A",
                "B",
                "C",
                "D",
                "E",
            ],
            "student_email": [
                "A@gmail.com",
                "B@gmail.com",
                "C@gmail.com",
                "D@gmail.com",
                "E@gmail.com",
            ]
        }
    )

    return students_df


def students_main_func():
    ColoredHeader(
        label="Students",
        description="Listing all the students"
    )

    # ADDING CONNECTION HERE
    # sample
    # conn = st.experimental_connection("sql")

    # temp
    conn = None

    students_df = get_students_data(conn)

    df = dataframe_explorer(students_df)
    st.dataframe(df)


if __name__ == "__main__":
    students_main_func()
