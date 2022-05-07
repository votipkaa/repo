import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('NFL Project')
st.markdown("## Bennie's First Data Science Project to Join the Coastal Elite 🏈")

NFL_DATA = 'https://github.com/votipkaa/repo/blob/main/NFL%20Stats%202021-22%20Season.xlsx'
points = st.slider("How many points scored?",0,900,10)

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_excel(NFL_DATA, sheet_name='Teams', nrows=nrows)
    data = data.sort_values('Total Points Scored',ascending=False)
    data = data.set_index('Teams')
    data = data.dropna(axis=0,how='all')
    data = data['Total Points Scored']
    data = data[data>=points]
    return data

data = load_data(32)

st.write("Points Scored",points)
st.bar_chart(data)
st.write(data)

points = st.number_input("Teams that allowed fewer than this many points:",0,1000,900)

@st.cache(persist=True)
def points_allowed(nrows):
    points_allowed_data = pd.read_excel(NFL_DATA, sheet_name='Teams', nrows=nrows)
    points_allowed_data = points_allowed_data.sort_values('Total Points Allowed',ascending=False)
    points_allowed_data = points_allowed_data.set_index('Teams')
    points_allowed_data = points_allowed_data.dropna(axis=0,how='all')
    points_allowed_data = points_allowed_data[['Total Points Scored','Total Points Allowed','Points Differential']]
    points_allowed_data = points_allowed_data[points_allowed_data['Total Points Allowed']<=points]
    return points_allowed_data

points_allowed_data = points_allowed(32)

st.write("Points Allowed",points)
st.bar_chart(points_allowed_data['Total Points Allowed'])
st.write("Sorted by points differential:",points_allowed_data.sort_values('Points Differential',ascending=False))
