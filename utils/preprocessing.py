import pandas as pd

def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text).replace("\n", " ").replace("\r", " ").strip()
    text = " ".join(text.split())
    return text

def preprocess_reviews(input_path="data/reviews.csv",
                       output_path="data/clean_reviews.csv"):

    df = pd.read_csv(input_path, engine="python", on_bad_lines="skip")

    # Drop null reviews
    df = df.dropna(subset=["Review"])

    # Clean text
    df["clean_review"] = df["Review"].apply(clean_text)

    # Remove very short reviews (noise)
    df = df[df["clean_review"].str.len() > 30]

    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned reviews saved to {output_path}")

    return df