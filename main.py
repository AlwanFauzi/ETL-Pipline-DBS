from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_gsheet

# Ganti ini dengan ID spreadsheet milikmu dan nama sheet yang sesuai
SPREADSHEET_ID = '1m84h2vohzMVctjWTbGHviMpFyCsBhGHvumKajifGGaA'
SHEET_RANGE = 'Sheet1!A1'

def main():
    print("📦 Memulai proses ETL...")

    # Extract
    print("🔍 Mengekstrak data dari situs web...")
    raw_data = extract_data()
    print(f"✅ Data berhasil diambil: {len(raw_data)} produk")

    # Transform
    print("🧪 Mentransformasi data...")
    transformed_data = transform_data(raw_data)
    print(f"✅ Data berhasil dibersihkan: {len(transformed_data)} produk")

    # Load
    print("💾 Menyimpan data ke CSV dan Google Sheets...")
    save_to_csv(transformed_data, filename='products.csv')
    save_to_gsheet(transformed_data, spreadsheet_id=SPREADSHEET_ID, sheet_range=SHEET_RANGE)

    print("🚀 Proses ETL selesai!")

if __name__ == '__main__':
    main()
