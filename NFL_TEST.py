import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import requests as rq
from io import BytesIO


NFL_DATA = 'https://github.com/votipkaa/repo/blob/main/NFL%20Stats%202021-22%20Season.xlsx?raw=true'


def load_data(nrows):
    data = pd.read_excel(NFL_DATA, sheet_name='Teams', nrows=nrows)
    data = data.sort_values('Total Points Scored',ascending=False)
    data = data.set_index('Teams')
    data = data.dropna(axis=0,how='all')
    data = data['Total Points Scored']
    return data

data = load_data(32)

print(data)

def points_allowed(nrows):
    points_allowed_data = pd.read_excel(NFL_DATA, sheet_name='Teams', nrows=nrows)
    points_allowed_data = points_allowed_data.sort_values('Total Points Allowed',ascending=False)
    points_allowed_data = points_allowed_data.set_index('Teams')
    points_allowed_data = points_allowed_data.dropna(axis=0,how='all')
    points_allowed_data = points_allowed_data[['Total Points Scored','Total Points Allowed','Points Differential']]
    return points_allowed_data

points_allowed_data = points_allowed(32)

print(points_allowed_data)
