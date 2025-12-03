# 🎬 Movie Recommendation Software 
A Python-based recommendation system using content-based filtering.

## GOAL:
Take in a dataset of movies, have users choose a movie that they already like and use said movie to recommend a chosen number of movies to the user.

### HOW TO RUN:
- Must be on Python 3.11 (3.11 optimal for Streamlit, won't work with 3.14)
- Make sure to have these modules installed:
    - pandas
    - numpy
    - scikit-learn
    - streamlit
- Into terminal, type 'streamlit run src/interface.py'
- Web UI will open and show instructions on how to use website.

### APPROACH/METHODOLOGY:
- **Data Processing**
  - Load MovieLens dataset (movies.csv, ratings.csv)
  - Combine genres into a single text field per movie
  - Calculate average ratings to display with recommendations

- **Recommendation Algorithm**
  - TF-IDF vectorization on genre data
  - Cosine similarity to measure how similar movies are
  - Return top N most similar movies when user selects one

- **Frontend**
  - Streamlit web interface for browsing, filtering, and getting recommendations

## RESULTS:
Software works as intended, by having user choose a movie they already like and using that as the base case to our recommender, our system finds movies with high similarity scores and prints as many recommendations the user requests.
