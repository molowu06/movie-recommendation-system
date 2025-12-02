import streamlit as st
import pandas as pd
import numpy as np
import time

# Title and info
st.title("Movie Recommendation Software")
st.write("Creators: Mimo Molowu, Stephanie Rojas Gonzales, Bhavana Kakumanu")
st.write("EECE 2140: Computing Fundamentals for Engineers")

# List of movie genres
genres = [
    "Action","Adventure","Animation","Children's","Comedy","Crime","Documentary",
    "Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance",
    "Sci-Fi","Thriller","War","Western"
]

# Define the movie database with ratings
movies_database = {
    "movieA": {"genres": ["Action", "Fantasy"], "rating": 5},
    "movieB": {"genres": ["Action"], "rating": 3},
    "movieC": {"genres": ["Fantasy"], "rating": 1}
}

# Multiselect widget for genres
chosen_genres = st.multiselect(
    "What's your favorite movie genres?",
    genres
)

# Display ONE widget with filtered movies
if chosen_genres:
    st.write("### Your Selected Genres & Movies:")

    with st.container(border=True):
        # Display all genres as badges
        st.write("**Your Genres:**")
        badge_html = ""
        for genre in chosen_genres:
            badge_html += f'<span style="background-color:#4CAF50; color:white; padding:8px 16px; margin:5px; border-radius:20px; display:inline-block;">{genre}</span>'
        st.markdown(badge_html, unsafe_allow_html=True)

        st.write("---")

        # Filter movies that match ANY of the chosen genres
        matching_movies = []
        for movie, details in movies_database.items():
            movie_genres = details["genres"]
            rating = details["rating"]

            if any(genre in movie_genres for genre in chosen_genres):
                # Show which genres match
                matched_genres = [g for g in chosen_genres if g in movie_genres]
                matching_movies.append({
                    "name": movie,
                    "genres": matched_genres,
                    "rating": rating
                })

        # Sort by rating (highest first)
        matching_movies.sort(key=lambda x: x["rating"], reverse=True)

        # Create display strings with ratings
        movie_options = [
            f"{movie['name']} - ⭐ {movie['rating']}/5 ({', '.join(movie['genres'])})"
            for movie in matching_movies
        ]

        # One combined dropdown with all matching movies
        if movie_options:
            st.write(f"**Movies matching your genres (sorted by rating):** ({len(movie_options)} found)")
            selected_movie = st.selectbox(
                "Choose a movie:",
                movie_options,
                key="combined_movie_select"
            )

            if selected_movie:
                st.success(f"✅ You selected: **{selected_movie}**")
        else:
            st.warning("No movies found for these genres.")

else:
    st.info("Select one or more genres above.")

# dates (newest to oldest)
# dates (oldest to newest)
# genres
# ratings
# Alphabeticly
#
