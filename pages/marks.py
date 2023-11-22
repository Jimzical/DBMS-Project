import streamlit as st
from components.helper_components import ColoredHeader, make_connection
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from pages.create import get_student_name
from st_pages import add_page_title
import plost

def get_marks(conn,student_name):
    cursor = conn.cursor(buffered=True)
    cursor.execute("USE student_marks")
    cursor.execute("SELECT ID from student where Name = %s",(student_name,))
    id = cursor.fetchall()[0][0]
    cursor.execute("SELECT DISTINCT Course_ID from exam where student_id = %s",(id,))
    subjects = cursor.fetchall()
    subject_list = [i[0] for i in subjects]
    subject_marks = {}
    subject_marks['Exam'] = ['ISA1','ISA2','ESA']

    for i in subject_list:

        cursor.execute("SELECT ID,Marks from Exam where course_id = %s",(i,))
        records = cursor.fetchall()
        marks_list = []
        for j in records:
            marks_list.append(j[1])
        subject_marks[i] = marks_list
    print(subject_marks)

    df = pd.DataFrame(subject_marks)
    print(df)
    return df

            
            
       
    

   
    
    # TODO: use sql to get the marks data

    # sample
    # marks_df = conn.query("select * from marks")

    # temp
    # create a sample dataframe with data
    marks_df = pd.DataFrame(
        {
            "student_id": [1, 2, 3, 4, 5],
            "student_name": [
                "A",
                "B",
                "C",
                "D",
                "E",
            ],
            "elective_subject": [
                "Python",
                "Machine Learning",
                "Data Science",
                "Data Visualization",
                "Data Analytics",
            ],
            "isa1": [46, 20, 93, 18, 94],
            "isa2": [80,51, 55, 38, 53],
            "esa": [14, 80, 67, 78, 70],
        }
    )

    #return marks_df

def for_multiple_electives(df):
    # probaby wont need it anymore
    
    plost.bar_chart(
        data=df,
        bar="elective_subject",
        value="isa1",
        title="ISA1 Marks",
        color="elective_subject",
        height=500,
        width=1000,
        opacity=0.8,
        # use_container_width=True,
    )    

    plost.bar_chart(
        data=df,
        bar="elective_subject",
        value="isa2",
        title="ISA2 Marks",
        color="elective_subject",
        height=500,
        width=1000,
        opacity=0.8,
        # use_container_width=True,
    )

    plost.bar_chart(
        data=df,
        bar="elective_subject",
        value="esa",
        title="ESA Marks",
        color="elective_subject",
        height=500,
        width=1000,
        opacity=0.8,
        # use_container_width=True,
    )

def for_few_electives(df):
    subjects = []
    for i in df.columns: 
        subjects.append(i)
    subjects = subjects[1::]
    print(subjects)
    
    
    for i in subjects:
        st.subheader(i)
        temp = pd.DataFrame(columns = ["Exam","Marks"],data = [["ISA 1",df[i][0]], ["ISA 2",df[i][1]], ["ESA",df[i][2]]])
        plost.bar_chart(
            data=temp,
            bar="Exam",
            value="Marks",
            title="Marks",
            color="Exam",
            height=500,
            width=1000,
            opacity=0.8,
            use_container_width=True,
        )

        
        
        # st.subheader(row["elective_subject"])
        # temp = pd.DataFrame(columns=["Exam","Marks"],data=[["ESA",row["isa1"]],["isa2",row["isa2"]],["esa",row["esa"]]])
        # plost.bar_chart(
        #     data=temp,
        #     bar="Exam",
        #     value="Marks",
        #     title="Marks",
        #     color="Exam",
        #     height=500,
        #     width=1000,
        #     opacity=0.8,
        #     # use_container_width=True,
        # )
    pass
def marks_main_func():
    # ADDING CONNECTION HERE
    # sample
    # conn = st.experimental_connection("sql")

    # temp
    conn = make_connection()
    cursor = conn.cursor(buffered=True)
    

    st.subheader("Select Student")
    student_list = get_student_name(conn)
    student_name = st.selectbox("Select Student", student_list)

    marks_df = get_marks(conn,student_name)

    df = dataframe_explorer(marks_df)
    st.dataframe(df, use_container_width=True)
    
    st.divider()
    with st.expander("Bar Graphs",expanded=True):
        st.title("Best Visualisation for Few Electives")
        for_few_electives(df)
        # for_multiple_electives(df)

if __name__ == "__main__":
    add_page_title(layout="wide")
    marks_main_func()