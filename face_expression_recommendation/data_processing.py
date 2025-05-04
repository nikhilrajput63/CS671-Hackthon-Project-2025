import pandas as pd

# Load the dataset
df = pd.read_csv("/home/nikhil-kumar/Documents/face_recog/movies.csv")

# 1. Convert genre string to list
df["genre_list"] = df["genre"].apply(lambda x: [g.strip() for g in x.split(",")])

# 2. Function to map overview to one of the 7 fixed moods
def infer_mood_fixed(overview):
    overview = overview.lower()
    
    mood_keywords = {
        "angry": ["rage", "revenge", "corrupt", "fight", "angry", "battle"],
        "fear": ["fear", "escape", "terrifying", "horror", "haunted", "danger", "threat"],
        "neutral": ["normal", "journey", "daily", "life", "usual", "routine"],
        "sad": ["loss", "grief", "alone", "unhappy", "death", "cry", "tragedy"],
        "disgust": ["corrupt", "disgust", "sick", "dirty", "vulgar"],
        "happy": ["fun", "laugh", "joy", "love", "celebrate", "happy", "reunion", "comedy"],
        "surprise": ["unexpected", "twist", "shock", "sudden", "mystery", "investigation"]
    }
    
    for mood, keywords in mood_keywords.items():
        if any(word in overview for word in keywords):
            return mood
    
    return "neutral"  # fallback default

# 3. Apply mood inference
df["mood"] = df["overview"].apply(infer_mood_fixed)

# 4. Save to new CSV
df.to_csv("preprocessed_movies.csv", index=False)
print("New file 'preprocessed_movies.csv' created with 'genre_list' and 'mood' columns.")
