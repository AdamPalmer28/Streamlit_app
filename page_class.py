import numpy as np
import pandas as pd
import streamlit as st


class web_page:

    def __init__(self, title, name):
        
        
        self.name = name

        # page properties
        self.title = title
        self.icon = "👋"
        self.page_layout = "wide"
        self.sidebar_state = "collapsed"

        
        

        


    def run(self):
        "Runs the streamlit application"

        self.page_config = st.set_page_config(
                            page_title= self.name,
                            page_icon= self.icon,
                            layout = self.page_layout,
                            initial_sidebar_state = self.sidebar_state,
                                )
                            
        st.title(self.title)


        self.html_format()
        
        self.sidebar()

        

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