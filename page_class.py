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


    def page_selector(self, otherpages):

        pass

#class ho