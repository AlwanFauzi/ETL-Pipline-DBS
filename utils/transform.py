import pandas as pd
import re

def transform_data(data):
    """Mentransformasi data hasil ekstraksi menjadi DataFrame yang bersih."""
    df = pd.DataFrame(data)
    print(f"📊 Jumlah data mentah: {len(df)}")

    # --- Transformasi kolom price ---
    df['price'] = df['price'].astype(str).str.replace('$', '', regex=False)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['price'] = (df['price'] * 16000).round(2)

    # --- Transformasi kolom rating ---
    def extract_rating(val):
        if isinstance(val, str):
            match = re.search(r'(\d+(\.\d+)?)', val)
            if match:
                return float(match.group(1))
        elif isinstance(val, (int, float)):
            return float(val)
        return None

    df['rating'] = df['rating'].apply(extract_rating)

    # --- Transformasi kolom colors ---
    df['colors'] = df['colors'].astype(str).str.extract(r'(\d+)')
    df['colors'] = pd.to_numeric(df['colors'], errors='coerce')

    # --- Bersihkan kolom size & gender ---
    df['size'] = df['size'].apply(lambda x: str(x).replace('Size:', '').strip() if pd.notna(x) else x)
    df['gender'] = df['gender'].apply(lambda x: str(x).replace('Gender:', '').strip() if pd.notna(x) else x)

    # --- Hapus baris dummy produk jika ada ---
    condition = (
        (df['title'] == 'Unknown Product') &
        (df['price'] == 1600000.0) &
        (df['rating'] == 5.0) &
        (df['colors'] == 5) &
        (df['size'] == 'M') &
        (df['gender'] == 'Men')
    )
    before_filter = len(df)
    df = df[~condition]
    print(f"🧹 Menghapus baris dummy: {before_filter - len(df)} baris dihapus")

    # --- Drop baris yang memiliki nilai null penting ---
    before_dropna = len(df)
    df = df.dropna(subset=['price', 'rating', 'colors', 'size', 'gender'])
    print(f"🧼 Drop baris kosong: {before_dropna - len(df)} baris dihapus")

    # --- Ubah tipe data ---
    df['colors'] = df['colors'].astype(int)
    df['price'] = df['price'].astype(float)
    df['rating'] = df['rating'].astype(float)
    df['size'] = df['size'].astype(str)
    df['gender'] = df['gender'].astype(str)

    print(f"✅ Data siap digunakan: {len(df)} baris")
    return df
