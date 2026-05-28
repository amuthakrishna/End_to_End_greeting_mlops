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

    # Create processed folder
  #  os.makedirs("data/processed", exist_ok=True)

    # Save clean data
    data.to_csv(output_file_path, index=False)

    # Print clean data
    print(data.to_string(index=False))

    print("\nData preparation completed")


if __name__ == "__main__":
    prepare_data(
        "data/raw_data.csv",
        "data/clean_data.csv"
    )