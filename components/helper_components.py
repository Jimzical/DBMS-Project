import streamlit as st
from time import sleep
import mysql.connector 


def make_connection():
    try:

        conn = mysql.connector.connect(host = "localhost",
                                    
                                    user="root",
                                    password="root")

        if conn.is_connected():
            print("Connection successful")
            return conn
    except ConnectionError as e:
        print("Error while connecting to MySQL",e)
    
        


def ColoredHeader(label : str = "Cool title",description : str = " ",color_name : str = "gold",help : str = "", description_help : str = "") -> None:
    """
    -------------------------------------------
    Shows a header with a colored underline and an optional description.
    -------------------------------------------
    Parameters:
        label (str): The title of the header. [Default: "Cool title"]
        description (str): The description of the header. [Default: "Cool description"]
        color_name (str): The color of the underline. [Default: "gold"]
        help (str): The help text of the title. [Default: nothing]
        description_help (str): The help text of the description. [Default: nothing]
    
    Returns:
        None

    Examples:
        >>> colored_header("Cool title", "Cool description", "gold", "This is the help text of the title", "This is the help text of the description")
        >>> colored_header("Cool title", "Cool description", "gold")

    """
    st.title(
        body=label,
        help=help,
    )
    st.write(
        f'<hr style="background-color: {color_name}; margin-top: 0;'
        ' margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">',
        unsafe_allow_html=True,
    )
    if description:
        st.caption(description,help=description_help)
def Notif(type : str = "success",duration : int = 3, message : str = "None") -> None:
    '''
    -------------------------------------------
    Shows a notification for a few seconds
    -------------------------------------------
    Parameters:
        type (str): The type of the notification. [Default: "success"]
        duration (int): The duration of the notification. [Default: 3]
        message (str): The message of the notification. [Default: "None"]

    Returns:
        None

    Examples:
        >>> Notif("success", 3, "This is a success notification")
        >>> Notif("error", 2, "This is an error notification")
        >>> Notif("warning", 5, "This is a warning notification")
        >>> Notif("info", 3, "This is an info notification")
    '''
    if message == "None":
        message = type 

    if type == "success":
        notif = st.success(message)
    elif type == "error":
        notif = st.error(message)
    elif type == "warning":
        notif = st.warning(message)
    elif type == "info":
        notif = st.info(message)
    else:
        notif = st.write("Notif type not found")
    
    sleep(duration)
    notif.empty()