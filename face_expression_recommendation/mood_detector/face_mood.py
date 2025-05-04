from deepface import DeepFace

def detect_mood(image, neutral_threshold=70):
    try:
        result = DeepFace.analyze(image, enforce_detection=False)
        if isinstance(result, list) and len(result) > 0:
            emotions = result[0]['emotion']
            dominant_emotion = result[0]['dominant_emotion']
            neutral_value = emotions.get('neutral', 0)
            # if neutral confidence is above threshold, pick second highest
            if dominant_emotion == 'neutral' and neutral_value > neutral_threshold:
                # sort emotions by confidence descending
                sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
                if len(sorted_emotions) > 1:
                    dominant_emotion = sorted_emotions[1][0]
            return {'dominant_emotion': dominant_emotion, 'emotion': emotions}
        else:
            return {'dominant_emotion': 'unknown', 'emotion': {}}
    except Exception as e:
        print(f"Error detecting mood: {e}")
        return {'dominant_emotion': 'error', 'emotion': {}}
