import streamlit as st
import requests

# Page setup
st.set_page_config(
    page_title="EmotionAI",
    page_icon="✨",
    layout="centered"
)

# Custom CSS for a clean, light, polished UI
st.markdown("""
    <style>
    /* Main app container styling */
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }
    
    /* Header styling */
    .header-container {
        text-align: center;
        padding: 0rem 0 1.5rem 0;
    }
    .header-badge {
        background-color: #e0f2fe;
        color: #0284c7;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 0.75rem;
        letter-spacing: 0.5px;
    }
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.3rem;
        letter-spacing: -0.5px;
    }
    .subtitle {
        font-size: 1.05rem;
        color: #64748b;
        font-weight: 400;
    }

    /* Card styling */
    .css-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 1.5rem;
    }

    /* Text area enhancement */
    div[data-testid="stTextArea"] textarea {
        background-color: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 10px !important;
        color: #1e293b !important;
        font-size: 1rem !important;
        transition: border-color 0.2s, box-shadow 0.2s;
    }
    div[data-testid="stTextArea"] textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
    }

    /* Primary button styling */
    div[data-testid="stButton"] button {
        width: 100%;
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: #ffffff;
        border: none;
        padding: 0.7rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        transition: all 0.2s ease-in-out;
    }
    div[data-testid="stButton"] button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
        color: #ffffff;
    }

    /* Result pill badge */
    .prediction-badge {
        display: inline-flex;
        align-items: center;
        background: #ecfdf5;
        color: #065f46;
        border: 1px solid #a7f3d0;
        font-weight: 700;
        font-size: 1.25rem;
        padding: 0.5rem 1.25rem;
        border-radius: 9999px;
        text-transform: capitalize;
    }

    /* Probabilities row */
    .prob-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.25rem;
        font-size: 0.95rem;
    }
    .prob-name {
        font-weight: 600;
        color: #334155;
        text-transform: capitalize;
    }
    .prob-val {
        font-weight: 600;
        color: #2563eb;
    }
    </style>
""", unsafe_allow_html=True)

# Emotion icon helper
EMOTION_ICONS = {
    "happy": "😊",
    "joy": "😄",
    "sadness": "😢",
    "sad": "😔",
    "anger": "😡",
    "angry": "😠",
    "fear": "😨",
    "surprise": "😲",
    "love": "❤️",
    "neutral": "😐"
}

# Header Section
st.markdown("""
    <div class="header-container">
        <span class="header-badge">NLP EMOTION DETECTOR</span>
        <h1 class="main-title">EmotionAI</h1>
        <p class="subtitle">Understand the real sentiment and emotion hidden within your text</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="css-card">', unsafe_allow_html=True)

# Input Section inside a clean card container
with st.container():
    
    text = st.text_area(
        "Enter your text",
        placeholder="Type or paste your sentence here...",
        height=140,
        label_visibility="collapsed"
    )

    analyze_clicked = st.button("✨ Analyze Emotion", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

# Processing and Output Section
if analyze_clicked:
    if not text.strip():
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing emotion..."):
            try:
                BACKEND_URL = "https://sentiment-analysis-6yy5.onrender.com/"

                response = requests.post(
                f"{BACKEND_URL}/predict",
                json={"text": text}) 
                response.raise_for_status()
                result = response.json()

                # Card for Results
                st.markdown('<div class="css-card">', unsafe_allow_html=True)
                
                # Header & Detected Emotion
                st.markdown("<h4 style='color: #64748b; font-size: 0.85rem; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 0.6rem;'>Predicted Emotion</h4>", unsafe_allow_html=True)
                
                pred = result.get("prediction", "")
                icon = EMOTION_ICONS.get(pred.lower(), "🎯")

                st.markdown(
                    f'<div ><span class="prediction-badge">{icon} &nbsp;{pred}</span></div>',
                    unsafe_allow_html=True
                )
                
                st.markdown("<hr style='border: none; border-top: 1px solid #f1f5f9; margin: 1.25rem 0;'>", unsafe_allow_html=True)
                
                
                # Probabilities Section
                st.markdown("<h4 style='color: #0f172a; font-size: 1.1rem; font-weight: 700;'>Confidence Breakdown</h4>", unsafe_allow_html=True)

                for emotion, probability in result["probabilities"].items():
                    prob_float = float(probability)
                    st.markdown(
                        f"""
                        <div class="prob-header">
                            <span class="prob-name">{emotion}</span>
                            <span class="prob-val">{probability}%</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.progress(min(prob_float / 100, 1.0))

                st.markdown('</div>', unsafe_allow_html=True)

            except requests.exceptions.RequestException:
                st.error("Could not connect to the backend.")