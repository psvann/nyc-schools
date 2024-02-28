import streamlit as st
import plotly.express as px
import pandas as pd
import os

token = os.getenv('MAPBOX_TOKEN')
px.set_mapbox_access_token(token)

df = pd.read_csv("data/full_joined_original_nyc_schools_dataset.csv")
df_map = df[["location_name","LATITUDE","LONGITUDE","Personal Attention and Support","Student-Teacher Trust","Grades_final_text","Administrative_District_Name"]]
df_map["Student Teacher Trust (Normalized)"] = 1 / df_map['Student-Teacher Trust'].astype('int') / 100

fig = px.scatter_mapbox(df_map, 
                        lat="LATITUDE", 
                        lon="LONGITUDE", 
                        color="Personal Attention and Support", 
                        size="Student Teacher Trust (Normalized)",
                        hover_name="location_name",
                        color_continuous_scale=px.colors.sequential.RdBu, 
                        size_max=10, 
                        zoom=10)

st.title('NYC Public Schools: Survey Data')

st.plotly_chart(fig)