import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages
from pages.home import home_main_func
def pages():
    show_pages(
        [
        Page("pages/home.py", "Home", "🏠"),
        Page("pages/create.py", "Add Marks", "📝"),
        Page("pages/display.py", "Display", "📖"),
        ]
    )


def main():
    home_main_func()
    pages()
   


if __name__ == "__main__":
    main()