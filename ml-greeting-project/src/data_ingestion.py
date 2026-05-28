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
        {"id": 10, "text": "thanks", "label": "gratitude"}
    ]

    # Create data folder
    os.makedirs("data", exist_ok=True)

    # Convert to DataFrame
    data_df = pd.DataFrame(data)

    # Save CSV file
    data_df.to_csv(input_file_path, index=False)

    # Print clean output
    print(data_df.to_string(index=False))

    print("\nData ingestion completed")


if __name__ == "__main__":
    load_data("data/raw_data.csv")