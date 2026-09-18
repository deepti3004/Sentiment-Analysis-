# Sentiment Analysis NLP

A machine learning-based Natural Language Processing project for analyzing text and predicting the associated emotion.

The project uses a trained machine learning classification model, Bag of Words text vectorization, a FastAPI backend for serving predictions, and a Streamlit frontend for interacting with the model.

## 🚀 Features

* Text-based emotion prediction
* Natural Language Processing pipeline
* Bag of Words text vectorization
* Trained machine learning classification model
* FastAPI REST API
* Streamlit interactive frontend
* Clean and responsive light-themed UI
* Emotion-specific icons
* Confidence breakdown for all predicted emotions
* Probability visualization using progress bars
* API testing with Postman
* Separate frontend and backend architecture

## 🛠️ Tech Stack

### Machine Learning / NLP

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Jupyter Notebook
* Joblib

### Backend

* FastAPI
* Uvicorn
* Pydantic
* Joblib

### Frontend

* Streamlit
* Python
* Requests
* Custom CSS

### Tools

* Git
* GitHub
* Postman
* VS Code

## 📁 Project Structure

```text
Sentiment-Analysis-/

│
├── backend/
│   └── main.py
│
├── app.py
│
├── app.ipynb
├── emotion_model.pkl
├── bow_vectorizer.pkl
├── reverse_map.pkl
├── train.txt
├── requirements.txt
├── .gitignore
└── README.md
```

### Project Files

| File                 | Description                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| `app.py`             | Streamlit frontend for entering text and displaying emotion predictions |
| `backend/main.py`    | FastAPI backend responsible for serving the prediction API              |
| `app.ipynb`          | Jupyter Notebook containing the NLP and machine learning workflow       |
| `emotion_model.pkl`  | Trained emotion classification model                                    |
| `bow_vectorizer.pkl` | Saved Bag of Words vectorizer                                           |
| `reverse_map.pkl`    | Mapping of numerical predictions to emotion labels                      |
| `train.txt`          | Training dataset                                                        |
| `requirements.txt`   | Python dependencies                                                     |

## 🧠 Machine Learning Pipeline

The project follows the following workflow:

```text
Input Text
    ↓
Text Preprocessing
    ↓
Bag of Words Vectorization
    ↓
Trained ML Model
    ↓
Emotion Prediction
    ↓
Probability Calculation
    ↓
FastAPI Response
    ↓
Streamlit Frontend
```

The trained model and vectorizer are saved using Joblib and loaded by the FastAPI backend.

### Model Files

| File                 | Description                                        |
| -------------------- | -------------------------------------------------- |
| `emotion_model.pkl`  | Trained emotion classification model               |
| `bow_vectorizer.pkl` | Bag of Words vectorizer                            |
| `reverse_map.pkl`    | Mapping of numerical predictions to emotion labels |

## 🎨 Streamlit Frontend

The frontend is implemented using **Streamlit** through `app.py`.

The application provides a simple interface where users can enter or paste text and analyze its associated emotion.

### UI Features

#### NLP Emotion Detector

The application displays an `NLP EMOTION DETECTOR` header with the project name **EmotionAI**.

#### Text Input

Users can enter text through a large text area:

```text
Type or paste your sentence here...
```

#### Analyze Emotion

The **✨ Analyze Emotion** button sends the entered text to the FastAPI backend.

The frontend sends a `POST` request to:

```text
http://127.0.0.1:8000/predict
```

with the following JSON structure:

```json
{
  "text": "I am very happy today"
}
```

#### Predicted Emotion

After receiving the response, the Streamlit application displays the predicted emotion with a corresponding emoji.

Examples include:

| Emotion  | Icon |
| -------- | ---- |
| Happy    | 😊   |
| Joy      | 😄   |
| Sadness  | 😢   |
| Sad      | 😔   |
| Anger    | 😡   |
| Angry    | 😠   |
| Fear     | 😨   |
| Surprise | 😲   |
| Love     | ❤️   |
| Neutral  | 😐   |

#### Confidence Breakdown

The application also displays the probability associated with each emotion.

Each probability is represented using a progress bar, allowing users to visually understand the model's confidence distribution.

### Frontend Workflow

```text
User
 ↓
Enter Text in Streamlit
 ↓
Click "Analyze Emotion"
 ↓
POST /predict
 ↓
FastAPI Backend
 ↓
ML Model
 ↓
Prediction + Probabilities
 ↓
Streamlit
 ↓
Predicted Emotion
 ↓
Confidence Breakdown
```

## ⚙️ Backend Setup

### 1. Create a Virtual Environment

Make sure Python 3.12 is installed.

```bash
py -3.12 -m venv .venv
```

Activate it on Git Bash:

```bash
source .venv/Scripts/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI Server

From the project directory:

```bash
cd backend
python -m uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

## 🔌 API Endpoint

### POST `/predict`

The endpoint accepts text and returns the predicted emotion and its probability distribution.

### Request

```json
{
  "text": "I am very happy today"
}
```

### Example Response

```json
{
  "prediction": "happy",
  "probabilities": {
    "happy": 82.5,
    "sad": 5.2,
    "anger": 3.8,
    "fear": 2.1,
    "surprise": 4.4,
    "neutral": 2.0
  }
}
```

The exact response depends on the trained model and backend implementation.

### Testing with Postman

Start the FastAPI server and create a `POST` request:

```text
http://127.0.0.1:8000/predict
```

Select:

```text
Body → raw → JSON
```

Then provide:

```json
{
  "text": "I am very happy today"
}
```

Click **Send** to receive the model prediction.

## 💻 Streamlit Frontend Setup

Open another terminal while the FastAPI server is running.

From the project root:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser.

### Complete Setup

You need two terminals running simultaneously.

**Terminal 1 — FastAPI Backend**

```bash
cd backend
python -m uvicorn main:app --reload
```

**Terminal 2 — Streamlit Frontend**

```bash
streamlit run app.py
```

The Streamlit application communicates with the FastAPI backend through the `/predict` endpoint.

## 📓 Jupyter Notebook

The `app.ipynb` notebook contains the NLP and machine learning workflow, including model training and saving the trained components.

The trained components are saved as:

```text
emotion_model.pkl
bow_vectorizer.pkl
reverse_map.pkl
```

These files are then used by the FastAPI backend for making predictions.

## 🔄 Complete Application Architecture

```text
                  User
                    │
                    ▼
          ┌──────────────────┐
          │    Streamlit     │
          │     app.py       │
          └────────┬─────────┘
                   │
                   │ POST /predict
                   ▼
          ┌──────────────────┐
          │     FastAPI      │
          │    Backend       │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Bag of Words     │
          │   Vectorizer     │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │  ML Classifier   │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Emotion +        │
          │ Probabilities    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │    Streamlit     │
          │  Result Display  │
          └──────────────────┘
```

## 🔒 Files Not Committed to Git

The following files and directories should generally remain excluded from version control:

```text
.venv/
__pycache__/
*.pyc
.env
```

These should be handled through `.gitignore`.

## 🖥️ Application Screens

The Streamlit interface contains:

1. **EmotionAI Header**
2. **Text Input Area**
3. **Analyze Emotion Button**
4. **Predicted Emotion Card**
5. **Emotion Icon**
6. **Confidence Breakdown**
7. **Probability Progress Bars**
8. **Backend Connection Error Handling**

## 🚧 Future Improvements

* Integrate Gemini for AI-generated explanations of predictions
* Add sentiment analysis alongside emotion classification
* Add conversation/history support
* Improve model accuracy with additional training data
* Experiment with TF-IDF and transformer-based embeddings
* Add model performance visualizations
* Deploy the FastAPI backend and Streamlit frontend online
* Add authentication and user-specific prediction history

## ▶️ Running the Complete Application

### Step 1 — Activate Environment

```bash
source .venv/Scripts/activate
```

### Step 2 — Start Backend

```bash
cd backend
python -m uvicorn main:app --reload
```

### Step 3 — Start Streamlit

Open another terminal:

```bash
streamlit run app.py
```

### Step 4 — Open the Application

Open the Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

Enter a sentence and click:

```text
✨ Analyze Emotion
```

The application will send the text to the FastAPI backend and display the predicted emotion along with the confidence breakdown.

## 👩‍💻 Author

**Deepti Singh**

GitHub: [@deepti3004](https://github.com/deepti3004)
