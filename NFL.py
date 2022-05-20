import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import requests as rq
from io import BytesIO

st.title('NFL Project')
st.markdown("## 2021-22 Stats 🏈")

NFL_DATA = 'https://github.com/votipkaa/repo/blob/main/NFL%20Stats%202021-22%20Season.xlsx?raw=true'

points = st.number_input("How many points scored?",0,900,10)

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


st.write("---------------------------------------------------------")

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
st.write(points_allowed_data)

st.write("---------------------------------------------------------")

wins = st.number_input("Wins at home:",0,16,0)

@st.cache(persist=True)
def home_wins(nrows):
    home_wins_data = pd.read_excel(NFL_DATA, sheet_name='Teams', nrows=nrows)
    home_wins_data = home_wins_data.sort_values('Total Wins @ Home',ascending=False)
    home_wins_data = home_wins_data.set_index('Teams')
    home_wins_data = home_wins_data.dropna(axis=0,how='all')
    home_wins_data = home_wins_data[['Total Wins @ Home','Average Points @ Home','Average Points Away']]
    home_wins_data = home_wins_data[home_wins_data['Total Wins @ Home']>=wins]
    return home_wins_data

home_wins_data = home_wins(32)

st.write("Wins at Home",wins)
st.bar_chart(home_wins_data['Total Wins @ Home'])
st.write(home_wins_data)

st.write("---------------------------------------------------------")

awaywins = st.number_input("Wins playing Away:",0,16,0)

@st.cache(persist=True)
def away_wins(nrows):
    away_wins_data = pd.read_excel(NFL_DATA, sheet_name='Teams', nrows=nrows)
    away_wins_data = away_wins_data.sort_values('Total Wins Away',ascending=False)
    away_wins_data = away_wins_data.set_index('Teams')
    away_wins_data = away_wins_data.dropna(axis=0,how='all')
    away_wins_data = away_wins_data[['Total Wins Away','Average Points Away','Average Points @ Home']]
    away_wins_data = away_wins_data[away_wins_data['Total Wins Away']>=awaywins]
    return away_wins_data

away_wins_data = away_wins(32)

st.write("Wins Away",awaywins)
st.bar_chart(away_wins_data['Total Wins Away'])
st.write(away_wins_data)

st.write("---------------------------------------------------------")

bigwin = st.number_input("Biggest Single Game Win:",0,40,0)

@st.cache(persist=True)
def biggest_win(nrows):
    biggest_win_data = pd.read_excel(NFL_DATA, sheet_name='Teams', nrows=nrows)
    biggest_win_data = biggest_win_data.sort_values('Biggest Win',ascending=False)
    biggest_win_data = biggest_win_data.set_index('Teams')
    biggest_win_data = biggest_win_data.dropna(axis=0,how='all')
    biggest_win_data = biggest_win_data['Biggest Win']
    biggest_win_data = biggest_win_data[biggest_win_data>=bigwin]
    return biggest_win_data

                                      
biggest_win_data = biggest_win(32)

st.write("Biggest Single Game Win",bigwin)
st.bar_chart(biggest_win_data)
st.write(biggest_win_data)

st.write("---------------------------------------------------------")



pointsdiff = st.number_input("Average Points Differential:",-30,30,-30)

@st.cache(persist=True)
def points_diff(nrows):
    pd_data = pd.read_excel(NFL_DATA, sheet_name='Teams', nrows=nrows)
    pd_data = pd_data.sort_values('Average Points Differential',ascending=False)
    pd_data = pd_data.set_index('Teams')
    pd_data = pd_data.dropna(axis=0,how='all')
    pd_data = pd_data['Average Points Differential']
    pd_data = pd_data[pd_data>=pointsdiff]
    return pd_data

                                      
pd_data = points_diff(32)

st.write("Average Points Differential",pointsdiff)
st.bar_chart(pd_data)
st.write(pd_data)

st.write("---------------------------------------------------------")

totalyards = st.number_input("Total Yards of Offense:",0,8000,0)

@st.cache(persist=True)
def total_yard(nrows):
    ty_data = ty.read_excel(NFL_DATA, sheet_name='Teams', nrows=nrows)
    ty_data = ty_data.sort_values('Total Yards',ascending=False)
    ty_data = ty_data.set_index('Teams')
    ty_data = ty_data.dropna(axis=0,how='all')
    ty_data = ty_data[['Total Yards','Total Yards Allowed']]
    ty_data = ty_data[tr_data['Total Yards']>=totalyards]
    return ty_data

                                      
ty_data = total_yard(32)

st.write("Total Yards of Offense",totalyards)
st.bar_chart(ty_data)
st.write(ty_data)
