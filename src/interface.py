import streamlit as st
import pandas as pd
import numpy as np
import time
from interface_code import *


st.markdown("<h1 style='text-align: center;'>Movie Recomendation Software</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:24px;'>Mimo Olowu, Stephanie Rojas Gonzales, Bhavana Kakumanu</p>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size:24px;'>EECE2140: Computing Fundamentals for Engineers", unsafe_allow_html=True)

with st.container(border = True):
    st.header("Can't settle on a movie? Let us help!")
    st.subheader("Step One:")
    st.write("Choose the genres that interest you")
    st.subheader("Step Two:")
    st.write("Sort by rating, date or alphebetically")
    st.write("You now have a list of movies ready to be enjoyed!")
    st.subheader("Want to watch more movies similar to the one you picked?")
    st.write("Just select the amount you would like, and we will provide you with a list!")

st.write("  ")
st.write("  ")
st.write("<p style='text-align: center; font-size:24px;'>Let's Get Started! 🎬", unsafe_allow_html=True)
st.divider()
st.write("  ")
st.write("  ")


# List of movie genres
genres = [
    "Action","Adventure","Animation","Children","Comedy","Crime","Documentary",
    "Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance",
    "Sci-Fi","Thriller","War","Western"
]

# Movies database as a DataFrame
movies_df = cleaning_data(True)

#User chooses genres
with st.container(border=True):
    st.subheader("What are your favorite movie genres?")

    chosen_genres = st.multiselect(
        "",
        genres
    )

#Display filtered movie list

if chosen_genres:
    st.write("### Your Selected Genres & Movies:")

    with st.container(border = True):
        #Will show genres as badges
        st.write("**Your Genres:**")
        badge_html = ""
        for genre in chosen_genres:
            badge_html += f'<span style="background-color:#4CAF50; color:white; padding:8px 16px; margin:5px; border-radius:20px; display:inline-block;">{genre}</span>'
        st.markdown(badge_html, unsafe_allow_html = True)

        st.write("---")

        filtered_movies = filter_genres(movies_df, chosen_genres)

        option = st.selectbox(
            "How would you like to filter the movies?",
            ("Average Rating", "Newest to Oldest", "Oldest to Newest", "Alphabetically"),
            index = None,
            placeholder = "Select a filter method..."
        )

        st.write("You selected:", option)

        st.write("---")

        movie_options = []
        if option == "Average Rating":
            #sort by rating
            filtered_df = order_by_ratings(filtered_movies)
            movie_options = [
                f"{row['title']} - ⭐ {row['avg_rating']}/5 ({row['genres']})"
                for _, row in filtered_df.iterrows()]
        elif option == "Newest to Oldest":
            #sort by date (newest to oldest)
            filtered_df = order_by_newest(filtered_movies)
            movie_options = [
                f"{row['title']} - ⭐ {row['avg_rating']}/5 ({row['genres']})"
                for _, row in filtered_df.iterrows()]
        elif option == "Oldest to Newest":
            #sort by date (oldest to newest)
            filtered_df = order_by_oldest(filtered_movies)
            movie_options = [
                f"{row['title']} - ⭐ {row['avg_rating']}/5 ({row['genres']})"
                for _, row in filtered_df.iterrows()]
        else:
            #sort alphabetically
            filtered_df = order_alphabetically(filtered_movies)
            movie_options = [
                f"{row['title']} - ⭐ {row['avg_rating']}/5 ({row['genres']})"
                for _, row in filtered_df.iterrows()]

        if len(movie_options) > 0:
            st.write(f"**Movies matching your genres:** ({len(movie_options)} found)")
            selected_movie = st.selectbox(
                "Choose a Movie:",
                movie_options,
                key = "combined_movies_select"
            )
            if selected_movie:
                st.success(f"✅ You selected: **{selected_movie}**")

                #getting selected movie title
                movie_str_list = selected_movie.split("⭐")
                ugly_movie_title = movie_str_list[0]
                movie_title = ugly_movie_title[:-3]

                #st.write(f"movie title: {movie_title}") #test to see if title works

                #=======
                with st.container(border = True):
                    st.write("How many movies would you want recommended?")
                    num = st.number_input(
                        "Select a number:",
                        min_value=0,
                        max_value=9000,
                        step=1
                    )
                    st.write("You selected:", num, "movies")

                recommendations_df = movie_recommendations(movies_df, movie_title, num)

                #another way of showing recommendations
                #will display the recommendations
                #if not recommendations_df.empty:
                #    with st.container(border = True):
                #        st.write(f"Your {num} Recommended Movies:")
                #        st.dataframe(recommendations_df, width="stretch")
                #else:
                #    st.warning("No recommendations found.")

                count = 1
                if not recommendations_df.empty:
                    with st.container(border = True):
                        st.write(f"Your {num} Recommended Movies:")
                        for _, row in recommendations_df.iterrows():
                            st.write(f"**{count}. {row['title']}** - ⭐ {row['avg_rating']} ({row['genres']})")
                            st.write(f"Similarity Score: {row['similarity_score']}")
                            count += 1
                else:
                    st.warning("No recommendations found.")
            else:
                st.warning("No movies found for these genres.")
