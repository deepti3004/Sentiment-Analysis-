import { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeEmotion = async () => {
    if (!text.trim()) return;

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: text,
        }),
      });

      const data = await response.json();

      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Could not connect to backend");
    }

    setLoading(false);
  };

  return (
    <div className="app">

      <header>
        <h1>EmotionAI</h1>
        <p>Understand the emotion behind your text</p>
      </header>

      <main>

        {/* Input */}
        <div className="input-card">

          <textarea
            placeholder="Type your sentence here..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />

          <button
            onClick={analyzeEmotion}
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Analyze Emotion"}
          </button>

        </div>


        {/* Result */}
        {result && (
          <div className="result-card">

            <h2>Prediction</h2>

            <div className="prediction">
              <span>Detected Emotion</span>

              <strong>
                {result.prediction}
              </strong>
            </div>


            <h3>Emotion Probabilities</h3>

            <div className="probabilities">

              {Object.entries(result.probabilities).map(
                ([emotion, probability]) => (

                  <div
                    className="emotion-row"
                    key={emotion}
                  >

                    <div className="emotion-info">

                      <span>
                        {emotion}
                      </span>

                      <span>
                        {probability}%
                      </span>

                    </div>

                    <div className="progress">

                      <div
                        className="progress-bar"
                        style={{
                          width: `${probability}%`,
                        }}
                      />

                    </div>

                  </div>

                )
              )}

            </div>

          </div>
        )}

      </main>

    </div>
  );
}

export default App;