import streamlit as st
from st_pages import add_page_title
from components.helper_components import ColoredHeader
from streamlit_extras.dataframe_explorer import dataframe_explorer
from st_pages import add_page_title, add_indentation

import pandas as pd
def get_elective_date(conn):
    # TODO: use sql to get the elective data

    # sample
    # elective_df = conn.query("select * from elective")

    # temp
    # create a sample dataframe with data
    elective_df = pd.DataFrame(
        {
            "elective_id": [1, 2, 3, 4, 5],
            "elective_name": [
                "Python",
                "Machine Learning",
                "Data Science",
                "Data Visualization",
                "Data Analytics",
            ],
            "elective_description": [
                "Python is a programming language. It is used for many purposes like web development, data science, etc.",
                "Machine Learning is a field of study that gives computers the ability to learn without being explicitly programmed.",
                "Data Science is a field of study that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from data in various forms, both structured and unstructured, similar to data mining.",
                "Data Visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.",
                "Data Analytics is the science of analyzing raw data in order to make conclusions about that information. Many of the techniques and processes of data analytics have been automated into mechanical processes and algorithms that work over raw data for human consumption.",
            ],
            "elective_instructor": [
                "Dr. A",
                "Dr. B",
                "Dr. C",
                "Dr. D",
                "Dr. E",
            ],
            "elective_instructor_email": [
                "uni_A@gmail.com",
                "uni_B@gmail.com",
                "uni_C@gmail.com",
                "uni_D@gmail.com",
                "uni_E@gmail.com"
            ]
        }
    )

                


    return elective_df

def electives_main_func():
    # ADDING CONNECTION HERE
    # sample
    # conn = st.experimental_connection("sql")	

    # temp
    conn = None
    elective_df = get_elective_date(conn)

    df = dataframe_explorer(elective_df)
    st.dataframe(df)
    


if __name__ == "__main__":
    add_page_title()
    electives_main_func()