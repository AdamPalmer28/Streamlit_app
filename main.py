import numpy as np
import pandas as pd
import streamlit as st

from page_class import *

from pages import *

def main():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.sidebar.success("Select a demo above.")

    st.title("Main")

if __name__ == '__main__':
    main()
