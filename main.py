import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st

from datetime import datetime

df  = pd.read_csv("cleaned_data.csv")
# st.set_page_config(layout="wide")
st.title(
    "Car Accident Data Visualization"
)
# st.write(df)
df['Accident Date'] = pd.to_datetime(df['Accident Date'])

st.column_config.ImageColumn(label=None, width='None', help=None)

st.subheader("Number Of Accident By Time ")
tab1,tab2= st.tabs(["Daily","Monthly"])

with tab1 : 
    selected_month = st.selectbox('Select Month', range(1, 13), format_func=lambda x: datetime.strptime(str(x), "%m").strftime("%B"))

    unique_years = sorted(df['Accident Date'].dt.year.unique())

    selected_year = st.selectbox('Select Year', unique_years, index=len(unique_years)-1,key="Option1")  # Select the last year by default

    filtered_df = df[(df['Accident Date'].dt.month == selected_month) & (df['Accident Date'].dt.year == selected_year)]


    total_accident= filtered_df.resample('D', on='Accident Date').size()
    total_accident.index=total_accident.index.strftime('%d %b')

    fig,ax=plt.subplots()
    total_accident.plot(kind='bar',ax=ax)
    ax.set_xlabel('Accident Date')
    ax.set_ylabel('Total Accident')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with tab2 : 
    unique_years2 = sorted(df['Accident Date'].dt.year.unique())

    selected_year2 = st.selectbox('Select Year', unique_years2, index=len(unique_years2)-1,key="Option2")  


    filtered_df = df[(df['Accident Date'].dt.year == selected_year2)]


    total_accident= filtered_df.resample('M', on='Accident Date').size()
    total_accident.index=total_accident.index.strftime('%b')

    fig,ax=plt.subplots()
    total_accident.plot(kind='bar',ax=ax)
    ax.set_xlabel('Accident Date')
    ax.set_ylabel('Total Accident')
    plt.xticks(rotation=45)
    st.pyplot(fig)


st.subheader("Number Of Accident By Severity And Vehicle Type ")
col1, col2, = st.columns([1,1])

with col1 : 

    Accident_Severity = df['Accident_Severity'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(Accident_Severity, labels=Accident_Severity.index, autopct='%1.1f%%', startangle=180, pctdistance=0.85)
    ax.set_title('Distribution of Accident by Accident_Severity')
    st.pyplot(fig)

with col2 : 
    fig, ax = plt.subplots()
    Vehicle_Type = df.groupby('Vehicle_Type').size()
    # Police_Force.index=Police_Force.index.strftime('%d %b')
    Vehicle_Type.plot(kind='bar',ax=ax)
    ax.set_xlabel('Vehicle_Type')
    ax.set_ylabel('Total Accident')
    
    ax.set_title('Distribution of Accident by Vehicle_Type')
    st.pyplot(fig)


st.subheader("Number Of Casualities And Vehicle ")

tab3,tab4= st.tabs(["Casualities","Vehicle Number"]) 

with tab3 : 
    selected_month = st.selectbox('Select Month', range(1, 13), format_func=lambda x: datetime.strptime(str(x), "%m").strftime("%B"),key="key1")

    unique_years = sorted(df['Accident Date'].dt.year.unique())

    selected_year = st.selectbox('Select Year', unique_years, index=len(unique_years)-1,key="Option3")  # Select the last year by default

    filtered_df = df[(df['Accident Date'].dt.month == selected_month) & (df['Accident Date'].dt.year == selected_year)]


    total_casuality = filtered_df.resample('D', on='Accident Date')['Number_of_Casualties'].sum()
    total_casuality.index=total_casuality.index.strftime('%d %b')

    fig,ax=plt.subplots()
    total_casuality.plot(kind='bar',ax=ax)
    ax.set_xlabel('Accident Date')
    ax.set_ylabel('Total Casualities')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with tab4: 
    selected_month = st.selectbox('Select Month', range(1, 13), format_func=lambda x: datetime.strptime(str(x), "%m").strftime("%B"),key="key2")

    unique_years = sorted(df['Accident Date'].dt.year.unique())

    selected_year = st.selectbox('Select Year', unique_years, index=len(unique_years)-1,key="Option4")  # Select the last year by default

    filtered_df = df[(df['Accident Date'].dt.month == selected_month) & (df['Accident Date'].dt.year == selected_year)]


    total_vehicles = filtered_df.resample('D', on='Accident Date')['Number_of_Vehicles'].sum()
    total_vehicles.index=total_vehicles.index.strftime('%d %b')

    fig,ax=plt.subplots()
    total_vehicles.plot(kind='bar',ax=ax)
    ax.set_xlabel('Accident Date')
    ax.set_ylabel('Total Vehicle')
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.subheader("Number Of Accident By Locations ")
col3, col4, = st.columns([2,1])

with col3 : 
    
    
    fig, ax = plt.subplots()
    Police_Force = df.groupby('Police_Force').size()
    # Police_Force.index=Police_Force.index.strftime('%d %b')
    Police_Force.plot(kind='bar',ax=ax)
    ax.set_xlabel('Police_Force')
    ax.set_ylabel('Total Vehicle')
    # plt.xticks(rotation=55) 
    ax.set_title('Distribution of Accident by Police_Force')
    st.pyplot(fig)

with col4 : 
    fig, ax = plt.subplots()
    Loc_Auth = df.groupby('Local_Authority_(District)').size().reset_index(name='Total')
    Loc_Auth.rename(columns={'Local_Authority_(District)': 'Local_Authority'}, inplace=True)
    
    Loc_Auth.columns=['District','Total']
    
    st.dataframe(Loc_Auth, width=290, height=470)

    
st.subheader("Number Of Accident By Conditions ")
col5,col6 =st.columns([1,1])

with col5 :
    Light_Con = df['Light_Conditions'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(Light_Con, labels=['']*len(Light_Con), autopct='', startangle=180, pctdistance=.35)
    ax.legend(Light_Con.index, loc='lower left',fontsize='small')
    ax.set_title('Distribution of Accident by Light_Conditions')
    st.pyplot(fig)


with col6 :
    Road_Surface_Conditions = df['Road_Surface_Conditions'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(Road_Surface_Conditions, labels=['']*len(Road_Surface_Conditions), autopct='', startangle=180, pctdistance=.35)
    ax.legend(Road_Surface_Conditions.index, loc='lower left',fontsize='small')
    ax.set_title('Distribution of Accident by Road_Surface_Conditions')
    st.pyplot(fig)
