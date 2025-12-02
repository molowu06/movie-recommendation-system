"""core recommender algorithm using content-based filtering"""
from typing import List, Tuple, Optional
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    """content-based movie recommender algorithm using TF-IDF & cosine similarity"""
    def __init__(self, movies_df: pd.DataFrame):
        """initialize the recommender with preprocessed movie data"""
        # copying to avoid modifying og dataframe
        self.movies_df = movies_df.copy()

        # initialize TF-IDF vectorizer
        self.tfidf = TfidfVectorizer(
            stop_words='english',
            lowercase=True,
            max_features=100
        )

        # check if preprocessor created preprocessed_genres column
        if 'processed_genres' not in self.movies_df.columns:
            # if not, create it by replacing '|' with spaces
            self.movies_df['processed_genres'] = self.movies_df['genres'].str.replace('|', ' ')

        #replace any missing genres with empyty string
        # fillna to prevent errors when processing
        self.movies_df['processed_genres'] = self.movies_df['processed_genres'].fillna('')

        # fit & transform the genres data
        # creates TF-IDF matrix: rows = movies, columns = genre words
        self.tfidf_matrix = self.tfidf.fit_transform(self.movies_df['processed_genres'])

        # compute cosine similarity matrix
        # results in a square matrix
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def _find_movie_index(self, title: str) -> Optional[int]:
        """find movie index by title (case-insensitive, partial match)"""
        # try exact match first
        exact_match = self.movies_df[self.movies_df['title'].str.lower() == title.lower()]
        if not exact_match.empty:
            #return the index of the first match
            return exact_match.index[0] # gets the actual index in the dataframe

        #if no exact match, try partial match
        partial_match = self.movies_df[self.movies_df['title'].str.contains(
            title, case=False, na=False)]
        if not partial_match.empty:
            return partial_match.index[0]

        # no match
        return None

    def get_similar_movies(self, movie_title: str, n: int = 5) -> pd.DataFrame:
        """get n most similar movies to the given movie"""
        # find the index of the requested movie
        movie_idx = self._find_movie_index(movie_title)

        #if movie not found, return empty dataframe
        if movie_idx is None:
            return pd.DataFrame()

        # get similarity scores for this movie vs all others
        # this is just one row from the similarity matrix
        sim_scores = self.similarity_matrix[movie_idx]

        # get indices sorted by value, by default ascending, so reverse it
        similar_indices = np.argsort(sim_scores)[::-1]

        # skip first index since it's the movie itself (get next n movies)
        similar_indices = similar_indices[1:n+1]

        # get full movie info for these indices
        similar_movies = self.movies_df.iloc[similar_indices].copy()

        # add similarity scores as a new column
        similar_movies['similarity_score'] = sim_scores[similar_indices]

        #select which columns to return
        columns = ['title', 'genres', 'similarity_score']
        #include rating it it exists
        if 'avg_rating' in similar_movies.columns:
            columns.insert(2, 'avg_rating')

        return similar_movies[columns]

    def get_recommendations_from_multiple(
            self, movie_titles: List[str], n: int = 5) -> pd.DataFrame:
        """get recommendations base on multiple input movies"""
        # TODO: figure out how to properly implement this
        pass

    def get_recommendations_from_filtered(
            self,
            movie_title: str,
            filtered_df: pd.DataFrame,
            n: int = 5) -> pd.DataFrame:
        """get recs based on a filtered dataframe of movies"""
        pass
        # may or may not need if we do not end up implementing tab 3
