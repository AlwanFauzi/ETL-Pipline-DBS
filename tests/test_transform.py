import pandas as pd
from utils import transform

def test_transform_data_cleaning():
    raw_data = [{
        "title": "Test Product",
        "price": "$10",
        "rating": "Rating: 4.2",
        "colors": "2 colors",
        "size": "Size: M",
        "gender": "Gender: Men"
    }]
    df = transform.transform_data(raw_data)

    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 1
    assert df.iloc[0]['price'] == 160000.0
    assert df.iloc[0]['rating'] == 4.2
    assert df.iloc[0]['colors'] == 2
    assert df.iloc[0]['size'] == "M"
    assert df.iloc[0]['gender'] == "Men"
