import streamlit as st
from components.helper_components import ColoredHeader, Notif,make_connection
import pandas as pd

def heading():
    ColoredHeader(
        label="Delete Items",
        description="Add marks for a student",
        color_name="gold",
        help="",
        description_help=""
    )