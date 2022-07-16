import numpy as np
import pandas as pd
import streamlit as st


class web_page:

    def __init__(self, title, name):
        
        self.title = title
        self.name = name


    def run(self):
        "Runs the streamlit application"
        st.title(self.title)

        # st.set_page_config(
        # page_title= self.name,
        # page_icon="👋",
        # )


    def page_selector(self, otherpages):

        pass

#class ho