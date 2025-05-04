import os

# Define the directory structure
directory_structure = {
    "MoodFlixx": {
        "app.py": "",
        "mood_detector": {
            "__init__.py": "",
            "face_mood.py": "",
        },
        "recommender": {
            "__init__.py": "",
            "suggestor.py": "",
        },
        "utils": {
            "text_mood.py": "",
        },
        "data": {
            "movies.csv": "",  # You can add a sample CSV file later
        },
        "requirements.txt": "",
        "README.md": "",
    }
}

# Function to create directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Create the MoodFlixx directory structure
create_structure(".", directory_structure)
