import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages
# from pages.home import home_main_func
def pages():
    # -----------------------------------------
    # TODO: Fix the section indentation stuff
    # -----------------------------------------
    show_pages(
        [
        Page("pages/home.py", "Home", "🏠"),
        Page("pages/create.py", "Add Marks", "📝"),
        Section("Display", icon=":mag:"),
        Page("pages/electives.py", "Electives", "📚", in_section = True ),
        Page("pages/instructors.py", "Instructors", "👨‍🏫"),
        Page("pages/students.py", "Students", "👨‍🎓"),
        Page("pages/marks.py", "Marks", "📝")
        ]
    )


def main():
    # home_main_func()
    pages()
   


if __name__ == "__main__":
    main()