import os
import joblib
import numpy as np
import glob

# Base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_DIR = os.path.join(BASE_DIR, "model")

# Get latest model automatically
model_files = glob.glob(os.path.join(MODEL_DIR, "intent_model_*.pkl"))

if not model_files:
    raise FileNotFoundError("No trained model found in model/ directory")

latest_model_path = max(model_files, key=os.path.getctime)

print(f"Loading model: {latest_model_path}")

model = joblib.load(latest_model_path)

# Input
text = input("Enter text: ").lower().strip()

# Prediction
probs = model.predict_proba([text])[0]
prediction = model.predict([text])[0]

confidence = np.max(probs)

# Threshold
THRESHOLD = 0.34

#print(f"Confidence Score: {confidence:.2f}")

if confidence < THRESHOLD:
    print("Prediction: Unknown / Not in dataset")
else:
    print("Prediction:", prediction)