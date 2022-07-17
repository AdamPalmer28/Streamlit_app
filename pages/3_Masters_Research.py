import numpy as np
import pandas as pd
import streamlit as st

from page_class import *

from tools.pdf_viewer import *


mast_p = web_page("K-Hyperplane Clustering problem", "Masters")
mast_p.run()


#st.write("Demo text")

#st.image("pages/resources/3_resources/Rot3.jpg")

displayPDF("pages/HyperplaneClustering.pdf")


if st.button("View PDF"):
    displayPDF("pages/resources/3_resources/HyperplaneClustering.pdf")
    st.write("Finished")

