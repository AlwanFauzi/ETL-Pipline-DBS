import pytest
import pandas as pd
from utils.transform import transform_data

def test_transform_data():
    raw_data = [
        {"title": "Product 1", "price": "$10", "rating": "4.5", "colors": "3 Colors", "size": "Size: M", "gender": "Gender: Unisex"},
        {"title": "Product 2", "price": "$20", "rating": "4.0", "colors": "2 Colors", "size": "Size: L", "gender": "Gender: Male"},
        {"title": "Product 3", "price": "$15", "rating": "5", "colors": "1 Color", "size": "Size: S", "gender": "Gender: Female"},
    ]

    df = transform_data(raw_data)

    # Periksa jumlah baris
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3

    # Periksa nilai yang ditransformasikan
    assert df['price'].iloc[0] == 160000
    assert df['rating'].iloc[0] == 4.5
    assert df['colors'].iloc[0] == 3
    assert df['size'].iloc[0] == "M"
    assert df['gender'].iloc[0] == "Unisex"

    assert df['price'].iloc[1] == 320000
    assert df['rating'].iloc[1] == 4.0
    assert df['colors'].iloc[1] == 2
    assert df['size'].iloc[1] == "L"
    assert df['gender'].iloc[1] == "Male"

    assert df['price'].iloc[2] == 240000
    assert df['rating'].iloc[2] == 5.0
    assert df['colors'].iloc[2] == 1
    assert df['size'].iloc[2] == "S"
    assert df['gender'].iloc[2] == "Female"
