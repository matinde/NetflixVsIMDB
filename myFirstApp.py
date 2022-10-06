import streamlit as st
import pandas as pd


netflix_df = pd.read_csv('NetflixOriginals.csv', encoding= 'latin-1')

st.title('Netflix Original Movies')
st.subheader('A close look at Netflix Original Movies as compared to IMDB ratings')

my_slider = st.slider('Select a range of values that will correspondent to IMDB Ratings for the films', 0.0, 10.0, (2.0, 8.0))

mask = netflix_df['IMDB Score'].between(my_slider[0], my_slider[1])

st.sidebar.title('User Input Features')


st.write(netflix_df[mask])