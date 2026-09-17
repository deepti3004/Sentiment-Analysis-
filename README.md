# Sentiment Analysis NLP

A machine learning-based Natural Language Processing project for analyzing text and predicting the associated emotion.

The project includes a trained machine learning model, text vectorization using Bag of Words, a FastAPI backend for serving predictions, and a React frontend for interacting with the model.

## 🚀 Features

* Text-based emotion prediction
* Natural Language Processing pipeline
* Bag of Words text vectorization
* Trained machine learning classification model
* FastAPI REST API
* React + Vite frontend
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

### Backend

* FastAPI
* Uvicorn
* Pydantic
* Joblib

### Frontend

* React
* Vite
* JavaScript
* HTML
* CSS

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
├── emotion-ui/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
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
API Response
    ↓
React Frontend
```

The trained model and vectorizer are saved using Joblib and loaded by the FastAPI backend.

### Model Files

| File                 | Description                                        |
| -------------------- | -------------------------------------------------- |
| `emotion_model.pkl`  | Trained emotion classification model               |
| `bow_vectorizer.pkl` | Bag of Words vectorizer                            |
| `reverse_map.pkl`    | Mapping of numerical predictions to emotion labels |

## ⚙️ Backend Setup

### 1. Create a virtual environment

Make sure Python 3.12 is installed.

```bash
py -3.12 -m venv .venv
```

Activate it on Git Bash:

```bash
source .venv/Scripts/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI server

```bash
cd backend
python -m uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### API Endpoint

```text
POST /predict
```

The endpoint accepts text and returns the predicted emotion.

You can test the API using Postman.

## 💻 Frontend Setup

Open a second terminal:

```bash
cd emotion-ui
npm install
npm run dev
```

Vite will provide a local development URL, usually:

```text
http://localhost:5173
```

The React frontend communicates with the FastAPI backend to obtain emotion predictions.

## 🔌 API Testing with Postman

Start the FastAPI server and create a `POST` request:

```text
http://127.0.0.1:8000/predict
```

Select:

```text
Body → raw → JSON
```

Then provide the input expected by the API.

Example:

```json
{
  "text": "I am very happy today"
}
```

Click **Send** to receive the model prediction.

## 📓 Jupyter Notebook

The `app.ipynb` notebook contains the NLP and machine learning workflow, including model training and saving the trained components.

The generated model files are then used by the FastAPI backend.

## 🔒 Files Not Committed to Git

The following files/directories should generally remain excluded from version control:

```text
.venv/
node_modules/
__pycache__/
*.pyc
.env
dist/
```

These are handled through `.gitignore`.

## ▶️ Running the Complete Application

Run the backend in one terminal:

```bash
cd backend
python -m uvicorn main:app --reload
```

Run the frontend in another terminal:

```bash
cd emotion-ui
npm run dev
```

Then open the React application in your browser.

```text
React Frontend
      ↓
FastAPI Backend
      ↓
Text Vectorizer
      ↓
ML Model
      ↓
Emotion Prediction
      ↓
FastAPI Response
      ↓
React UI
```

## 👩‍💻 Author

**Deepti Singh**

GitHub: [@deepti3004](https://github.com/deepti3004)
