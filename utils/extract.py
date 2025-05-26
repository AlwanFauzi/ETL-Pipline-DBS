import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
BASE_URL = "https://fashion-studio.dicoding.dev"

def get_html(page_number):
    if page_number == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}/page{page_number}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"[!] Gagal mengambil halaman {page_number}: {e}")
        return None

def parse_product(card):
    def get_text(element, default=''):
        return element.text.strip() if element else default

    title = get_text(card.find('h3', class_='product-title'))
    price = get_text(card.find('span', class_='price'))

    p_tags = card.find_all('p')
    rating = get_text(p_tags[0]).replace('Rating:', '') if len(p_tags) > 0 else ''
    color = get_text(p_tags[1]) if len(p_tags) > 1 else ''
    size = get_text(p_tags[2]).replace('Size:', '') if len(p_tags) > 2 else ''
    gender = get_text(p_tags[3]).replace('Gender:', '') if len(p_tags) > 3 else ''

    return {
        'title': title,
        'price': price,
        'rating': rating,
        'colors': color,
        'size': size,
        'gender': gender
    }

def extract_data():
    all_products = []

    for page in range(1, 51):  # Loop 50 halaman
        print(f"🔍 Mengambil halaman {page}...")
        html = get_html(page)
        if not html:
            continue

        soup = BeautifulSoup(html, 'html.parser')
        cards = soup.find_all('div', class_='collection-card')

        for card in cards:
            product_info = parse_product(card)
            all_products.append(product_info)

        time.sleep(1)  # Hindari terlalu cepat request

    return all_products
