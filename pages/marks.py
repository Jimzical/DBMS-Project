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
    print(subject_list)
    for i in subject_list:

        cursor.execute("SELECT ID,Marks from Exam where course_id = %s and student_id = %s",(i,id))
        records = cursor.fetchall()
        print(i,records)
        marks_list = []
        for j in records:
            marks_list.append(j[1])
        subject_marks[i] = marks_list
    print(subject_marks)

    print(subject_marks)
    df = pd.DataFrame(subject_marks)
    print(df)
    return df

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

# def calculate_avg_marks(course_code):
#     conn = make_connection()
#     cursor = conn.cursor()
#     cursor.execute("USE student_marks")

#     query = f"SELECT AVG(marks) AS avg_marks FROM exam WHERE course_id = '{course_code}'"
    
#     cursor.execute(query)
#     result = cursor.fetchone()

#     conn.close()

#     if result and result[0] is not None:
#         avg_marks = result[0]
#         return pd.DataFrame({'Course Code': [course_code], 'Average Marks': [avg_marks]})
#     else:
#         return pd.DataFrame({'Course Code': [course_code], 'Average Marks': [None]})
def calculate_avg_marks(course_code):
    conn = make_connection()
    cursor = conn.cursor()
    cursor.execute("USE student_marks")

    query = f"SELECT AVG(marks) AS avg_marks FROM exam WHERE course_id = '{course_code}'"
    
    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    if result and result[0] is not None:
        avg_marks = result[0]
        return pd.DataFrame({'Course Code': [course_code], 'Average Marks': [avg_marks]})
    else:
        return pd.DataFrame({'Course Code': [course_code], 'Average Marks': [None]})


def marks_main_func():
    conn = make_connection()
    cursor = conn.cursor(buffered=True)
    

    st.subheader("Select Student")
    student_list = get_student_name(conn)
    student_name = st.selectbox("Select Student", student_list)

    marks_df = get_marks(conn,student_name)
    st.dataframe(marks_df, use_container_width=True)

    st.subheader("Stats")
    # st.write(marks_df.describe())
    # check if marks_df has more than one col
    if len(marks_df.columns) > 1:
        for i in marks_df.columns[1::]:
            st.dataframe(calculate_avg_marks(i))
    st.divider()
    with st.expander("Bar Graphs",expanded=True):
        st.title("Visualisation for Electives")
        for_few_electives(marks_df)
        # for_multiple_electives(df)
    





if __name__ == "__main__":
    add_page_title(layout="wide")
    marks_main_func()