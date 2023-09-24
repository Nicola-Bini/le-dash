from lib.ConnectFunctions import get_today_analytics
import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame(get_today_analytics())   
df['date2'] = df['date'].apply(lambda x: pd.to_datetime(x).date())
df['date'] = df['date'].apply(lambda x: pd.to_datetime(x).date())
df = df.set_index('date')
print(df.index)

st.title('LE Analytics')
main, likes, users, resources, libraries, categories = st.tabs(["Main", "Likes", 'Users', 'Resources', 'Libraries', 'Categories'])


with main:

    settings_row1 = st.columns([2,1,1])

    # Align text to center
    settings_row1[0].text('Last Update: '+ str(df.index[-1]))
    selected_option = settings_row1[2].selectbox('Delta change', ['daily', 'monthly'], index=0,  key=None, help=None, on_change=None, placeholder="Choose an option", disabled=False, label_visibility="visible")

    st.markdown('#')

    if selected_option == 'daily':
        daily_change_reference = 'DailyChange'
    else:
        daily_change_reference = 'MonthlyChange'

    metrics_row1 = st.columns(5)
    metrics = [{'label': 'Likes', 'value': round(df['totalNumberOfLikes'].iloc[-1]), 'delta': round(df['totalNumberOfLikes' + daily_change_reference].iloc[-1]) if 'totalNumberOfLikes' + daily_change_reference in df.columns else np.NaN},
               {'label': 'Resources', 'value': round(df['totalNumberOfResources'].iloc[-1]), 'delta': round(df['totalNumberOfResources' + daily_change_reference].iloc[-1]) if 'totalNumberOfResources' + daily_change_reference in df.columns else np.NaN},
               {'label': 'Categories', 'value': round(df['totalNumberOfCategories'].iloc[-1]), 'delta': round(df['totalNumberOfCategories' + daily_change_reference].iloc[-1]) if 'totalNumberOfCategories' + daily_change_reference in df.columns else np.NaN},
               {'label': 'Users', 'value': round(df['totalNumberOfRegisteredUsers'].iloc[-1]), 'delta': round(df['totalNumberOfRegisteredUsers' + daily_change_reference].iloc[-1]) if 'totalNumberOfRegisteredUsers' + daily_change_reference in df.columns else np.NaN},
               {'label': 'Libraries', 'value': round(df['totalNumberOfLibraries'].iloc[-1]), 'delta': round(df['totalNumberOfLibraries' + daily_change_reference].iloc[-1]) if 'totalNumberOfLibraries' + daily_change_reference in df.columns else np.NaN}]

    for i, metric in enumerate(metrics):
        metrics_row1[i].metric(metric['label'], metric['value'], delta=metric['delta'], delta_color="normal", help=None, label_visibility="visible")
    


with likes:
    st.line_chart(df, x='date2',  y='totalNumberOfLikes')

with users:
    st.line_chart(df,  y='totalNumberOfRegisteredUsers')

with resources:
    st.line_chart(df,  y='totalNumberOfResources')

with libraries:
    st.line_chart(df,  y='totalNumberOfLibraries')

with categories:
    st.line_chart(df,  y='totalNumberOfCategories')
