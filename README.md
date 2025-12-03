# movie-recommendation-system
A Python-based recommendation system using content-based filtering.

GOAL:
Take in a data set of movies, have users choose a movie that they already like and use said movie to recommend a chosen number of movies to the user.

HOW TO RUN:
- Be on Python 3.11 (3.11 optimal for Streamlit, won't work with 3.14)
- Make sure to have these modulos downloaded:
    - pandas
    - numpy
    - scikit-learn
    - streamlit
- Into terminal, type 'streamlit run src/interface.py'
- Web UI will open and show instructions on how to use website.

REQUIREMENTS OR DEPENDENCIES:
NOT DONE

APPROACH/METHODOLOGY:
NOT DONE

RESULTS:
Code works perfectly, by having user choose a movie they already like and using that as the base case to our recommender, our system finds movies with high similarity scores and prints as many recommendations the user request.
