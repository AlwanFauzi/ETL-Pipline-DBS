import pytest
from utils import extract

def test_get_html():
    html = extract.get_html(1)
    assert html is not None
    assert "<html" in html.lower()

def test_parse_product_structure():
    sample_html = """
    <div class="collection-card">
        <h3 class="product-title">Test Product</h3>
        <span class="price">$100</span>
        <p>Rating: 4.5</p>
        <p>3 colors available</p>
        <p>Size: L</p>
        <p>Gender: Unisex</p>
    </div>
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(sample_html, 'html.parser')
    product = extract.parse_product(soup)
    
    assert product['title'] == "Test Product"
    assert product['price'] == "$100"
    assert product['rating'] == "4.5"
    assert product['colors'] == "3 colors available"
    assert product['size'] == "L"
    assert product['gender'] == "Unisex"
