import streamlit as st
import pandas as pd
from plotly import express as px


netflix_df = pd.read_csv('NetflixOriginals.csv', encoding= 'latin-1')

st.set_page_config(page_title='Netflix Originals vs IMDB', 
                page_icon=':tv:', 
                layout='wide', 
                initial_sidebar_state='auto'
                )

st.title('Netflix Original Movies')
st.subheader('A close look at Netflix Original Movies as compared to IMDB ratings (up to 2020)')

col1, col2, col3, col4 = st.columns(4)
col1.metric('Total Movies', netflix_df.shape[0])
col2.metric('Highest rated genre', netflix_df['Genre'].value_counts().index[0])
col3.metric('Highest IMDB Rating', netflix_df['IMDB Score'].max())
col4.metric('Lowest IMDB Rating', netflix_df['IMDB Score'].min())

#Create a plotly chart where people can select the genre
st.sidebar.title('Summary')
st.sidebar.markdown('''
    With a growing libary of original movies, moving to and from IMDB to find a 
    suitable weekend movie can be a husssle. With this visualization, you can find a
    well rated movie for you pleasure. IMDB ratings are not the holy grail of how good
    or bad a movie is but its one of the essential metrics used.
    ''')

st.sidebar.title('Top 5 Genres')
st.sidebar.write(netflix_df['Genre'].value_counts().index[:5])
#remove header and index

st.sidebar.title('Top 5 movies')
st.sidebar.write(netflix_df['Title'].value_counts().index[:5])


# create a multi-select box
genre = st.multiselect('Select Genre', netflix_df['Genre'].unique(), default=['Drama', 'Documentary'])


first_chart = px.scatter(netflix_df[netflix_df['Genre'].isin(genre)], 
                        x='IMDB Score', y='Genre', size='IMDB Score', 
                        color='IMDB Score', hover_name='Title', size_max=20, 
                        title='IMDB Score vs Genre'
                        )
st.plotly_chart(first_chart, use_container_width=True)


st.write('''
    Below is a full interactive table which you can find a range of information on the 
    ratings regardless of the genre. Uset the slider to filter the IMDB score on the movie
    list. 
    ''')
my_slider = st.slider('Select a range', 0.0, 10.0, (2.0, 8.0))

mask = netflix_df['IMDB Score'].between(my_slider[0], my_slider[1])



st.write(netflix_df[mask].sort_values('Title'), use_container_width=True)
