import streamlit as st
import pickle
import pandas as pd
import requests

def fethc_poster(movie_id):
  response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=600e8b20212b0c4a47702d7df90ab42d".format(movie_id))
  data=response.json()

  return "https://image.tmdb.org/t/p/w500"+ data['poster_path']
def recommendation(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  recommend_movies=[]
  recommend_movies_poster=[]
  for i in movies_list:
    recommend_movies.append(movies.iloc[i[0]].title)
    recommend_movies_poster.append(fethc_poster(movies.iloc[i[0]].movie_id))
  return recommend_movies,recommend_movies_poster


movies_dict=pickle.load(open("movies_dict.pkl","rb"))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open("similarity.pkl","rb"))
st.title("Movie Recommendation System")
selected_movies=st.selectbox("Write a movie name to get recommendation",
             movies['title'].values)

if st.button("Recommend"):
  names,poster=recommendation(selected_movies)
  col1, col2, col3 ,col4,col5= st.columns(5)
  with col1:
    st.text(names[0])
    st.image(poster[0])
  with col2:
    st.text(names[1])
    st.image(poster[1])
  with col3:
    st.text(names[2])
    st.image(poster[2])
  with col4:
    st.text(names[3])
    st.image(poster[3])
  with col5:
    st.text(names[4])
    st.image(poster[4])