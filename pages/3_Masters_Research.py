import numpy as np
import pandas as pd
import streamlit as st

from page_class import *

from tools.pdf_viewer import *


mast_p = web_page("K-Hyperplane Clustering problem", "Masters")
mast_p.run()



if st.button("View PDF"):
    displayPDF("pages/resources/3_resources/HyperplaneClustering.pdf")
    st.write("Finished")

