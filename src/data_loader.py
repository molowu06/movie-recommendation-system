"""file for movies & ratings data loading functions"""
from typing import Optional
import pandas as pd

def load_movies(movies_path: str) -> pd.DataFrame:
    """loads movies from the given filepath"""
    movies_df = pd.read_csv(movies_path)
    return movies_df

def load_ratings(ratings_path: str) -> pd.DataFrame:
    """loads ratings from the given filepath"""
    ratings_df = pd.read_csv(ratings_path)
    return ratings_df

def avg_ratings(ratings_df: pd.DataFrame) -> pd.DataFrame:
    """calculates the average rating for per movie"""
    avg_ratings_df = ratings_df.groupby('movieId')['rating'].mean().reset_index()
    avg_ratings_df.rename(columns={'rating': 'avg_rating'}, inplace=True)
    return avg_ratings_df

def merge_movies_ratings(movies_df: pd.DataFrame, avg_ratings_df: pd.DataFrame) -> pd.DataFrame:
    """merging the movies & ratings dataframes based on their movie ids"""
    merged_df = pd.merge(movies_df, avg_ratings_df, on='movieId')
    return merged_df

def movie_id_lookup(movies_df: pd.DataFrame, title: str) -> Optional[int]:
    """returns movie id when given movie title"""
    matches = movies_df[movies_df['title'] == title]
    if not matches.empty:
        return int(matches.iloc[0]['movieId'])
    return None
