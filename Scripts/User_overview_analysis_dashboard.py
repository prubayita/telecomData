import pandas as pd
import streamlit as st
import sys
sys.path.append('../scripts')

#load the data to be used
sys.path.append('./data')
data_df=pd.read_csv('../data/user_overview.csv')

#create the containers on the page
header = st.container()
handset_types = st.container()
manufacturers=st.container()
handset_manufacturers = st.container()
visualization = st.container()



with header:
    st.title("User Overview Analysis")
    
    
with handset_types:
    st.header("Top 10 handset used by customers")
    df=data_df['Handset Type'].value_counts().reset_index(name="count")
    df.columns = ['Handset Type', 'Total Handsets']
    st.write(df.head(10))
with manufacturers:
    st.header("Top 3 handset manufacturers")
    df=data_df['Handset Manufacturer'].value_counts().reset_index(name="count")
    df.columns = ['Handset Manufacturer', 'Total Handsets']
    st.write(df.head(3))
    
    
with handset_manufacturers:
    st.header("Top 5 handsets by top 3 handset manufacturers")