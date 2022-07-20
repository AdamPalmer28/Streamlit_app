import numpy as np
import pandas as pd
import streamlit as st

from page_class import *

from tools.pdf_viewer import *


mast_p = web_page("K-Hyperplane Clustering problem", "Masters")
mast_p.run()



with st.expander("My idea"):
    st.image("pages/resources/3_resources/Rot3.jpg", width = 600, caption = "My formulation for linearising the hypersphere")


if st.button("View PDF"):
    displayPDF("pages/resources/3_resources/HyperplaneClustering-compressed.pdf")
    st.write("Finished")

