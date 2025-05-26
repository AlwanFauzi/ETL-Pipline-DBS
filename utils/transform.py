import pandas as pd
import re

EXCHANGE_RATE = 16000  # USD to IDR

def clean_price(price_str):
    try:
        return round(float(price_str.replace('$', '')) * EXCHANGE_RATE, 2)
    except:
        return None

def extract_numeric(text):
    match = re.search(r'(\d+(\.\d+)?)', str(text))
    return float(match.group(1)) if match else None

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)
    print(f"[INFO] Data loaded: {len(df)} rows")

    # Clean price
    df['price'] = df['price'].apply(clean_price)

    # Clean rating
    df['rating'] = df['rating'].apply(extract_numeric)

    # Extract number of colors
    df['colors'] = df['colors'].apply(lambda x: int(extract_numeric(x) or 0))

    # Normalize size and gender
    df['size'] = df['size'].str.strip().replace('', 'Unknown')
    df['gender'] = df['gender'].str.strip().replace('', 'Unknown')

    # Drop rows with invalid price or rating
    df.dropna(subset=['price', 'rating'], inplace=True)

    return df
