import numpy as np
import pandas as pd
import streamlit as st


class web_page:

    def __init__(self, title, name):
        
        self.title = title
        self.name = name

        self.page_config = st.set_page_config(
                            page_title= self.name,
                            page_icon= "👋",
                            layout = "wide",
                            initial_sidebar_state = "expanded",
                                )


        self.html_format()
        
        self.sidebar()

        


    def run(self):
        "Runs the streamlit application"
        st.title(self.title)

        # st.set_page_config(
        # page_title= self.name,
        # page_icon="👋",
        # )

    def sidebar(self):
        with st.sidebar:
            add_selectbox = st.selectbox(
                "How would you like to be contacted?",
                ("Email", "Home phone", "Mobile phone")
            )

    def html_format(self):

        #
        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)


        


#class ho