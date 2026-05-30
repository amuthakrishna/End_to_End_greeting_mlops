import pandas as pd
import os

def prepare_data(input_file_path, output_file_path):

    # Read data
    data = pd.read_csv(input_file_path)

    # Remove duplicates
    data = data.drop_duplicates()

    # Remove null values
    data = data.dropna()

    # Convert text to lowercase
    data["text"] = data["text"].str.lower()

    # Remove id column
    data = data.drop(columns=["id"])

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Save clean data
    data.to_csv(output_file_path, index=False)

    print(data.to_string(index=False))
    print("\nData preparation completed")


if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_path = os.path.join(base_dir, "data", "raw_data.csv")
    output_path = os.path.join(base_dir, "data", "clean_data.csv")

    prepare_data(input_path, output_path)