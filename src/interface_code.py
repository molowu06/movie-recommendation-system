from typing import Optional
import pandas as pd
import numpy as np
from data_loader import *
from preprocessor import clean_genres
from preprocessor import extract_year
from recommender import *

def cleaning_data(b: bool) -> pd.DataFrame:
    if b:
        movies_df = load_movies("data/ml-latest-small/movies.csv")
        ratings_df = load_ratings("data/ml-latest-small/ratings.csv")
        avg_ratings_df = avg_ratings(ratings_df)
        merge_df = merge_movies_ratings(movies_df, avg_ratings_df)
        merge = clean_genres(merge_df)
        clean_movies = extract_year(merge)
    return clean_movies

def filter_genres(movies: pd.DataFrame, genres_chosen: list[str]) -> Optional[pd.DataFrame]:
    """Will filter through the movies dataframe for movies that have at least one of the genres
    the user had chosen"""
    #makes genres list into a single string so that pandas can iterate when filtering
    pattern = "|".join(genres_chosen)
    movies_filtered = movies[movies.apply(lambda row: row.astype(str).str.contains(pattern, case = False, na = False).any(), axis = 1)]
    return movies_filtered

def order_by_oldest(movies: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Will order all of the movies by oldest to youngest, no years will be at end"""
    return movies.sort_values('year')

def order_by_newest(movies: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Will order all of the movies by youngest to oldest, no years will be at end"""
    return movies.sort_values('year', ascending = False)

def order_by_ratings(movies: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Will order all of the movies by the average rating"""
    return movies.sort_values('avg_rating', ascending = False)

def order_alphabetically(movies: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Will order all of the movies alphabetically"""
    return movies.sort_values('title')

def movie_recommendations(movies: pd.DataFrame, movie_title: str, num_of_recs: int) -> pd.DataFrame:
    """Will take in the entire movie list (or filtered list), movie title user wants to use
    for their recommendations, and the number of recomendations they want, and give back a Dataframe
    containing n amount of movies (including their title, genres it contains, and similarity score)"""
    obj1 = MovieRecommender(movies)
    recommendations = obj1.get_similar_movies(movie_title, num_of_recs)
    return recommendations

