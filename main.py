import streamlit as st
import pandas as pd
import pickle


import requests
# apikey="6523e15edd4d7b83c6e3a17335c41a01"
#
# url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
# # url = "https://api.themoviedb.org/3/find/{}?external_source=imdb_id&language=en-US".format[movie_id]
# # url="https://api.themoviedb.org/3/movie/{}?external_source=imdb_id&language=en-US".format
# headers = {
#     "accept": "application/json",
#     "Authorization": apikey
# }
# #url = "https://api.themoviedb.org/3/find/{}?external_source=imdb_id&language=en-US".format[movie_id]
# #
# # response = requests.get(url, headers=headers)



# def fetch_posters(movie_id):
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
#     st.text(data)



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=6523e15edd4d7b83c6e3a17335c41a01&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index=movies_dict[movies_dict["title"] == movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x : x[1])[1:6]

    recommend_movies=[]
    recommend_movie_posters=[]

    for i in movie_list:
        movie_id=movies_dict.iloc[i[0]].movies_id
        recommend_movies.append(movies_dict.iloc[i[0]]["title"])  #here we get the names using just the id
        recommend_movie_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movie_posters

movies_dict=pickle.load(open("movies_dict.pkl",'rb'))
# movies=pd.DataFrame(movies_dict)


similarity=pickle.load(open("similarity.pkl",'rb'))



st.title("This is a movie recommending system  ")
# st.title("_Streamlit_ is :blue[cool] :sunglasses:")
# st.title("Dashboard", icon=":material/dashboard:")
movie_list = movies_dict['title'].values

option = st.selectbox(
    "How would you like to be contacted?",
    # movies["title"].values
     movie_list
)

if st.button("recommend"):
   # recommendations=recommend(option)
    names,posters=recommend(option)   # for i in recommendations: #     st.write(i)
    col1,col2,col3,col4,col5= st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])



