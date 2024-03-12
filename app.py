import streamlit as st
import plotly.express as px
import pandas as pd
import os

token = os.getenv('MAPBOX_TOKEN')
px.set_mapbox_access_token(token)

st.set_page_config(layout='wide')
st.markdown("""<style> .reportview-container { top: 0px; } </style>""", unsafe_allow_html=True)


df = pd.read_csv("data/full_joined_original_nyc_schools_dataset.csv")

df_map = df[["location_name","Grades_final_text","LATITUDE","LONGITUDE","Personal Attention and Support","Student-Teacher Trust","Administrative_District_Name"]]

# school_type = st.selectbox('Select School Type', 
#                            df_map['Grades_final_text'].unique() )
# filtered_df = df[df['Grades_final_text'] == school_type]

filtered_df = df_map[df_map['Grades_final_text'].str.contains('07',na=False)]

filtered_df["Student Teacher Trust (Normalized)"] = 100 - filtered_df['Student-Teacher Trust'].astype('int')

filtered_df["Personal Attention and Support (Normalized)"] = 100 - filtered_df['Personal Attention and Support'].astype('int')

fig = px.scatter_mapbox(filtered_df, 
                        lat="LATITUDE", 
                        lon="LONGITUDE", 
                        # color="Personal Attention and Support", 
                        size="Personal Attention and Support (Normalized)",
                        hover_name="location_name",
                        hover_data=["location_name","Grades_final_text","Personal Attention and Support (Normalized)","Student Teacher Trust (Normalized)"],
                        # color_continuous_scale=px.colors.sequential.RdBu, 
                        size_max=10, 
                        zoom=10,
                        height=800)

st.header('NYC Public Schools: Survey Data')

st.plotly_chart(fig, use_container_width=True, height=800)