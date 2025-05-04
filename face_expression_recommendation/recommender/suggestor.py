import pandas as pd

def load_movies(movie_path):
    try:
        movies = pd.read_csv(movie_path)
        return movies
    except Exception as e:
        print(f"Error loading movies: {e}")
        return None

def recommend_movies(movies, mood):
    try:
        # Check if the mood column exists
        if 'mood' not in movies.columns:
            print("Error: 'mood' column not found in the dataset.")
            return None
        
        # Filter recommendations based on mood
        recommendations = movies[movies['mood'].apply(lambda x: mood.lower() in x)].head(7)  # Limit to 7 movies
        return recommendations if not recommendations.empty else None
    except Exception as e:
        print(f"Error getting recommendations: {e}")
        return None

def get_recommendations(movie_data, mood):
    return recommend_movies(movie_data, mood)
