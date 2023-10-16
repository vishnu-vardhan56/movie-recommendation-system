import streamlit as st
import pickle


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list2 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_moives = []
    for i in movies_list2:
        recommend_moives.append(movies_list.iloc[i[0]].title)
    return recommend_moives
similarity = pickle.load((open('similarity.pkl','rb')))
movies_list = pickle.load(open('movies.pkl','rb'))
movies_list1 = movies_list['title'].values
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    (movies_list1)
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)