import numpy as np
import pandas as pd
import streamlit as st

from page_class import *

from pages import *


class webapp:

    def __init__(self):
        
        

        # Hide mainmenu and footer
        homepage = web_page("Welcome to my Home Page", "Homepage")
        homepage.run()

        st.sidebar.success("Select a demo above.")




if __name__ == '__main__':
    homepage = webapp()
