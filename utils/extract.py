import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://fashion-studio.dicoding.dev"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_html(page_number):
    """Mengambil HTML dari halaman tertentu dengan format URL yang sesuai."""
    if page_number == 1:
        url = f"{BASE_URL}/"
    else:
        url = f"{BASE_URL}/page{page_number}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"[!] Gagal mengambil halaman {page_number}: {e}")
        return None

def parse_product(card):
    """Mengurai informasi produk dari elemen HTML kartu produk."""
    def get_text(element, default=''):
        return element.text.strip() if element else default

    title = get_text(card.find('h3', class_='product-title'))
    price = get_text(card.find('span', class_='price'))

    p_tags = card.find_all('p')
    rating = get_text(p_tags[0]).replace('Rating:', '').strip() if len(p_tags) > 0 else ''
    colors = get_text(p_tags[1]).strip() if len(p_tags) > 1 else ''
    size = get_text(p_tags[2]).replace('Size:', '').strip() if len(p_tags) > 2 else ''
    gender = get_text(p_tags[3]).replace('Gender:', '').strip() if len(p_tags) > 3 else ''

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "colors": colors,
        "size": size,
        "gender": gender
    }

def extract_data():
    """Menjalankan proses ekstraksi data dari semua halaman."""
    all_products = []

    for page in range(1, 51):
        print(f"🔍 Mengambil halaman {page}...")
        html = get_html(page)
        if not html:
            continue

        soup = BeautifulSoup(html, 'html.parser')
        cards = soup.find_all('div', class_='collection-card')

        for card in cards:
            product_info = parse_product(card)
            all_products.append(product_info)

        time.sleep(1)

    return all_products
