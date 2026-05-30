import pandas as pd
import os

def load_data(input_file_path):
    data = [
        {"id": 1, "text": "hiii", "label": "greeting"},
        {"id": 2, "text": "hello", "label": "greeting"},
        {"id": 3, "text": "good morning", "label": "greeting"},
        {"id": 4, "text": "bye", "label": "goodbye"},
        {"id": 5, "text": "see you later", "label": "goodbye"},
        {"id": 6, "text": "how are you", "label": "question"},
        {"id": 7, "text": "what is your name", "label": "question"},
        {"id": 8, "text": "what time is it", "label": "question"},
        {"id": 9, "text": "thank you", "label": "gratitude"},
        {"id": 10, "text": "thanks", "label": "gratitude"},
        {"id": 11, "text": "i appreciate it", "label": "gratitude"},
        {"id": 12, "text": "good night", "label": "goodbye"},
        {"id": 13, "text": "see you tomorrow", "label": "goodbye"},
        {"id": 14, "text": "what's up", "label": "greeting"},
        {"id": 15, "text": "how's it going", "label": "greeting"},
        {"id": 16, "text": "i'm fine", "label": "response"},
        {"id": 17, "text": "not bad", "label": "response"},
        {"id": 18, "text": "could be better", "label": "response"},
        {"id": 19, "text": "i'm doing well", "label": "response"},
        {"id": 20, "text": "i'm good", "label": "response"}
    ]

    os.makedirs(os.path.dirname(input_file_path), exist_ok=True)

    data_df = pd.DataFrame(data)
    data_df.to_csv(input_file_path, index=False)

    print(data_df.to_string(index=False))
    print(f"\nData saved to: {input_file_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "raw_data.csv")

    load_data(csv_path)