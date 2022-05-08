import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import requests as rq
from io import BytesIO

st.title('NFL Project')
st.markdown("## Bennie's First Data Science Project to Join the Coastal Elite 🏈")

NFL_DATA = 'https://github.com/votipkaa/repo/blob/main/NFL%20Stats%202021-22%20Season.csv?raw=true'
data = pd.read_csv(NFL_DATA, nrows=32)

st.write(data)

