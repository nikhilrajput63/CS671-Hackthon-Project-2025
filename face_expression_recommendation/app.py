import streamlit as st
import cv2
import numpy as np
import pandas as pd
from mood_detector.face_mood import detect_mood
from recommender.suggestor import get_recommendations

# Load the movie dataset
movie_data = pd.read_csv("/home/nikhil-kumar/Documents/MoodFlixx/processed_movies.csv")
movie_data.columns = movie_data.columns.str.strip()

# Streamlit app
st.title("MoodFlixx - Mood-Based Movie Recommendations")
st.write("### Detect your mood and get personalized movie suggestions!")

# Start webcam
video_capture = cv2.VideoCapture(0)

# Manage webcam run state with session state
if 'run_webcam' not in st.session_state:
    st.session_state.run_webcam = False

if st.button("Start Webcam", key="start_webcam") and not st.session_state.run_webcam:
    st.session_state.run_webcam = True

if st.session_state.run_webcam:
    ret, frame = video_capture.read()
    if not ret:
        st.warning("Failed to capture image from webcam.")
        st.session_state.run_webcam = False
    else:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st.image(frame_rgb, channels="RGB")

        # Detect mood
        mood_results = detect_mood(frame_rgb)
        st.write(f"Raw Mood Detection Results: {mood_results}")
        mood = mood_results.get('dominant_emotion', "unknown")
        st.write(f"Detected Mood: {mood}")

        # Get recommendations (limit to top 7)
        recommendations = get_recommendations(movie_data, mood)
        if recommendations is not None and isinstance(recommendations, pd.DataFrame):
            st.markdown("### Recommended Movies:")
            for _, movie in recommendations.iterrows():
                col1, col2 = st.columns([1, 3])
                with col1:
                    # Optional: Display poster if poster_url in dataset (uncomment if you have this column)
                    # st.image(movie.get('poster_url', None), width=100)
                    # For now, display a placeholder icon
                    st.image("https://via.placeholder.com/100x150.png?text=No+Image", width=100)
                with col2:
                    st.subheader(movie['movie_name'])
                    st.markdown(f"**Year:** {movie.get('year', 'N/A')}")
                    st.markdown(f"**Genre:** {movie.get('genre', 'N/A')}")
                    st.markdown(f"**Overview:** {movie.get('overview', 'N/A')}")
                    st.markdown(f"**Director:** {movie.get('director', 'N/A')}")
                    st.markdown(f"**Cast:** {movie.get('cast', 'N/A')}")
        else:
            st.info("No recommendations available for this mood.")

        if st.button("Stop Webcam", key="stop_webcam"):
            st.session_state.run_webcam = False
            video_capture.release()
            cv2.destroyAllWindows()
            st.write("Webcam stopped.")
else:
    st.info("Press 'Start Webcam' to detect your mood and get recommendations.")
