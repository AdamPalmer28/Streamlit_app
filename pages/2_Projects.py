import numpy as np
import pandas as pd
import streamlit as st

from page_class import *




graphs_p = web_page("My current project", "Projects")
graphs_p.run()

av_tab, chess_tab, rubix_tab, con4_tab = st.tabs(["Algorithm visualiser","Chess engine", "3D game engine", \
                                    "Connect 4 neural network"])

with av_tab:
    st.subheader("Number sorting algorithm")


with chess_tab:
    st.subheader("Python - Chess engine")


with rubix_tab:
    st.subheader("My 3D engine")

    st.write()


with con4_tab:
    st.subheader("Connect 4 AI")

    st.write("")


with st.expander("Potential future projects:"):

    fp_text = """
    * Webscraping 
    * LBlockduko 
    """
    st.markdown(fp_text, unsafe_allow_html = True)
