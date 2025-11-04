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

def clean_genres(movies_df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """cleans the genres columns by replacing '(no genres listed)' with NaN & splits multiple genres with ',' not '|'"""
    pass

def prepare_features_for_tfidf(movies_df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """prepares the features for tfidf vectorization"""
    if isinstance(movies_df, pd.DataFrame):
        movies_df['processed_genres'] = movies_df['genres'].str.replace('|', ' ')
        return movies_df

def handle_missing_data(movies_df: pd.DataFrame, ratings_df: pd.DataFrame) -> Optional[tuple[pd.DataFrame, pd.DataFrame]]:
    """handles missing data in movies & ratings dataframes"""
    pass
