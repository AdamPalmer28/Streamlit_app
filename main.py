import numpy as np
import pandas as pd
import streamlit as st

from page_class import *

from pages import *


class webapp:

    def __init__(self):
        
        self.page_config = st.set_page_config(
                            page_title="Hello",
                            page_icon="👋",
                            layout = "wide",
                            initial_sidebar_state = "collapsed",
                            menu_items = {
                                    'Get Help': 'https://www.extremelycoolapp.com/help',
                                    'Report a bug': "https://www.extremelycoolapp.com/bug",
                                    'About': "# This is a header. This is an *extremely* cool app!"
                                    }
                                    )

        # Hide mainmenu and footer
        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
        #st.markdown(hide_streamlit_style, unsafe_allow_html=True)


        st.sidebar.success("Select a demo above.")

        st.title("Home Page")

if __name__ == '__main__':
    homepage = webapp()
