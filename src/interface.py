import streamlit as st
import pandas as pd
import numpy as np
import time
from data_loader import *

st.title("Movie Reccomendation Software")
st.write("Creators: Mimo Molowu, Stephanie Rojas Gonzales, Bhavana Kakumanu")
st.write( "EECE 2140: Computing Fundimentals for Engineers")


#st.radio is for one selection
#multiselect if for multiple

genres = ["Comedy", "Drama", "Documentary", "Sci-Fi", "Crime", "Romance", "Fantasy", "Animation", "Horror", "Action", "Thriller"]
chosen_genres = st.multiselect(
    "What's your favorite movie genres?",
    genres
)
st.write("### You selected:")
for genre in chosen_genres:
    st.markdown(f"- :orange[{genre}]")


movies_df = load_movies("data/ml-latest-small/movies.csv")
ratings_df = load_ratings("data/ml-latest-small/ratings.csv")
avg_ratings_df = avg_ratings(ratings_df)
merge_df = merge_movies_ratings(movies_df, avg_ratings_df)

print(merge_df)


# dates (newest to oldest)
# dates (oldest to newest)
# genres
# ratings
# Alphabeticly
#
