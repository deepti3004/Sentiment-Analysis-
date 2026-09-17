import os
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Load trained ML components
model = joblib.load(os.path.join(BASE_DIR, "emotion_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "bow_vectorizer.pkl"))
reverse_map = joblib.load(os.path.join(BASE_DIR, "reverse_map.pkl"))


# Request format
class TextInput(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Emotion Detection API is running"}


@app.post("/predict")
def predict_emotion(data: TextInput):

    # Convert input text into vector
    text_vector = vectorizer.transform([data.text])

    # Get probabilities
    probabilities = model.predict_proba(text_vector)[0]

    # Get predicted class
    prediction = model.predict(text_vector)[0]

    # Convert number → emotion name
    predicted_emotion = reverse_map[int(prediction)]

    # Create probability response
    emotions = {}

    for emotion_number, probability in zip(
        model.classes_,
        probabilities
    ):
        emotion_name = reverse_map[int(emotion_number)]

        emotions[emotion_name] = round(
            float(probability) * 100,
            2
        )

    return {
        "text": data.text,
        "prediction": predicted_emotion,
        "probabilities": emotions
    }