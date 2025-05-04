from textblob import TextBlob

def detect_text_mood(text):
    try:
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return "happy"
        elif analysis.sentiment.polarity < 0:
            return "sad"
        else:
            return "neutral"
    except Exception as e:
        print(f"Error detecting text mood: {e}")
        return "Unknown"