import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(
    BASE_DIR,
    "model",
    "intent_model_20260528_141632.pkl"
)

model = joblib.load(model_path)

text = input("Enter text: ").lower().strip()

probs = model.predict_proba([text])[0]

max_prob = np.max(probs)

prediction = model.predict([text])[0]

print(f"Confidence Score: {max_prob:.2f}")

THRESHOLD = 0.34

if max_prob < THRESHOLD:
    print("Prediction: The data is not available in the dataset.")
else:
    print("Prediction:", prediction)