import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

fichero = pd.read_csv("IMDB-Movie-Data.csv")

"""
# Welcome to Streamlit Albert!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_año = st.slider("Año de la película", fichero["Year"].values.min(), fichero["Year"].values.max())
num_ratio = st.slider("Rating", fichero["Rating"].values.min(), fichero["Rating"].values.max())



plt.plot(num_año,num_ratio)
