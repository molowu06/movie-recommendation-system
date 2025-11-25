"""cleaning up the data (removing duplicates, missing values, etc)"""
from typing import Optional
import pandas as pd

def extract_year(movies_df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """extracts year from movie title"""
    if isinstance(movies_df, pd.DataFrame):
        def get_year(title: str) -> Optional[int]:
            if '(' in title and ')' in title:
                year_str = title.split('(')[-1].split(')')[0]
                if year_str.isdigit():
                    return int(year_str)
            return None
        movies_df['year'] = movies_df['title'].apply(get_year)
        return movies_df
    return None

def clean_genres(movies_df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """cleans the genres columns by replacing '(no genres listed)' with NaN &
    splits multiple genres with ',' not '|'"""
    if isinstance(movies_df, pd.DataFrame):
        movies_df['genres'] = movies_df['genres'].replace('(no genres listed)', pd.NA)
        movies_df['genres'] = movies_df['genres'].str.replace('|', ',')
        return movies_df
    return None

def prepare_features_for_tfidf(movies_df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """prepares the features for tfidf vectorization"""
    if isinstance(movies_df, pd.DataFrame):
        movies_df['processed_genres'] = movies_df['genres'].str.replace('|', ' ')
        return movies_df
    return None

def handle_missing_data(movies_df: pd.DataFrame,
                        ratings_df: pd.DataFrame) -> Optional[tuple[pd.DataFrame, pd.DataFrame]]:
    """handles missing data in movies & ratings dataframes by removing them"""
    if isinstance(movies_df, pd.DataFrame) and isinstance(ratings_df, pd.DataFrame):
        movies_df = movies_df.dropna(subset=['title', 'genres'])
        ratings_df = ratings_df.dropna(subset=['userId', 'movieId', 'rating'])
        return movies_df, ratings_df
    return None

def remove_duplicates(movies_df: pd.DataFrame, ratings_df: pd.DataFrame) -> Optional[tuple[pd.DataFrame, pd.DataFrame]]:
    """removes duplicate entries in movies & ratings dataframes"""
    if isinstance(movies_df, pd.DataFrame) and isinstance(ratings_df, pd.DataFrame):
        movies_df = movies_df.drop_duplicates(subset=['movieId'])
        ratings_df = ratings_df.drop_duplicates(subset=['userId', 'movieId'])
        return movies_df, ratings_df
    return None

def add_metadata_columns(movies_df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """ add rating_count (how many people rated each movie)
    & add decade column ("1990s", "2000s", etc.)"""
    if not isinstance(movies_df, pd.DataFrame):
        return None

    #rating_count per movieId
    movies_df['rating_count'] = movies_df['movieId'].map(
            movies_df['movieId'].value_counts()
    )

    #helper that accepts numbers or NaN; returns None for missing/invalid years
    def get_decade(year: Optional[int]) -> Optional[str]:
        if year is None or (isinstance(year, float) and pd.isna(year)):
            return None
        try:
            y = int(year)
        except (ValueError, TypeError):
            return None
        decade_start = (y // 10) * 10
        return f"{decade_start}s"

    # derive decase from a 'year' column
    if 'year' in movies_df.columns:
        movies_df['decade'] = movies_df['year'].apply(get_decade)
    else:
        # create decade column as None if no year info
        movies_df['decade'] = None

    return movies_df
