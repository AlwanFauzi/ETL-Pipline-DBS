import pandas as pd
from utils import load
from unittest.mock import patch, MagicMock

def test_save_to_csv(tmp_path):
    df = pd.DataFrame([{"col1": "val1", "col2": "val2"}])
    file_path = tmp_path / "test.csv"
    
    load.save_to_csv(df, filename=file_path)
    assert file_path.read_text().startswith("col1,col2")

@patch("utils.load.Credentials.from_service_account_file")
@patch("utils.load.build")
def test_save_to_gsheet(mock_build, mock_creds):
    df = pd.DataFrame([{"col1": "val1", "col2": "val2"}])
    spreadsheet_id = "dummy_id"
    sheet_range = "Sheet1!A1"

    mock_service = MagicMock()
    mock_sheet = MagicMock()
    mock_service.spreadsheets.return_value = mock_sheet
    mock_build.return_value = mock_service

    load.save_to_gsheet(df, spreadsheet_id, sheet_range)

    mock_sheet.values().clear.assert_called_once()
    mock_sheet.values().update.assert_called_once()
