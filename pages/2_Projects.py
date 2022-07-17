import numpy as np
import pandas as pd
import streamlit as st

from page_class import *




graphs_p = web_page("My current project", "Projects")
graphs_p.run()

tab1, tab2, tab3, tab4 = st.tabs(["Algorithm visualiser","Chess engine", "3D game engine", "Connect 4 neural network"])

with tab1:
    st.header("Number sorting algorithm")