import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

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
num_revenue = st.slider("Revenue (Millions)", fichero["Revenue (Millions)"].values.min(), fichero["Revenue (Millions)"].values.max())


indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
