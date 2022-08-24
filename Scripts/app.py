import sys


import streamlit as st
from multiapp import MultiApp
from dashboard_pages import userOverview_analysis_dashboard, userEngagement_analysis_dashboard, userExperience_analysis_dashboard , userSatisfaction_analysis_dashboard
# import your app modules here

st.set_page_config(page_title="TellCo Data Analysis", layout="wide")

app = MultiApp()


st.sidebar.markdown("""
# TellCo's User Analytics
This Multipage app presents a detailed user analysis of Tellco. The analysis was based on the following key areas:
1. User Overview Analysis
2. User Engagement Analysis
3. User Experience Analysis
4. User Satisfaction Analyis

This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
### Modifications
\t- Page Folder Based Access

""")

# Add all your application here
app.add_app("User Overview Analysis", userOverview_analysis_dashboard.app)
app.add_app("User Engagement Analysis", userEngagement_analysis_dashboard.app)
app.add_app("User Experience Analysis", userExperience_analysis_dashboard.app)
app.add_app("User Satisfaction Analysis", userSatisfaction_analysis_dashboard.app)

# The main app
app.run()
