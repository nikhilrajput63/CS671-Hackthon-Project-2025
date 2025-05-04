from deepface import DeepFace
import numpy as np

def detect_mood(image):
    try:
        # Analyze the image
        result = DeepFace.analyze(image, enforce_detection=False)
        print("Detection Result:", result)  # Print the result for debugging

        # Check if the result is a list and has elements
        if isinstance(result, list) and len(result) > 0:
            emotions = result[0]['emotion']
            dominant_emotion = result[0]['dominant_emotion']
            print("Emotions Probabilities:", emotions)

            # Set a threshold for dominant emotion detection
            threshold = 10.0  # Adjust this threshold as needed
            detected_emotion = max(emotions, key=emotions.get)  # Get the emotion with the highest probability
            detected_probability = emotions[detected_emotion]

            # Print the detected emotion and its probability
            print(f"Detected Emotion: {detected_emotion} with probability: {detected_probability}")

            # Check if the detected emotion exceeds the threshold
            if detected_probability > threshold:
                return detected_emotion
            else:
                print("No dominant emotion detected above threshold.")
                return "Uncertain"
        else:
            print("No valid result returned.")
            return "Unknown"
    except Exception as e:
        print(f"Error detecting mood: {e}")
        return "Error"

# Example usage
image_path = "/home/nikhil-kumar/Documents/MoodFlixx/image.jpg"  # Replace with your image path
mood = detect_mood(image_path)
print(f"Detected Mood: {mood}")
