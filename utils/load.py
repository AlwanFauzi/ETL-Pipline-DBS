import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os

def save_to_csv(df, filename='products.csv'):
    try:
        df.to_csv(filename, index=False)
        print(f"[INFO] Saved to {filename}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save CSV: {e}")
        return False

def get_gsheet_service(credential_path='google-sheets-api.json'):
    if not os.path.exists(credential_path):
        raise FileNotFoundError(f"Credential file '{credential_path}' not found.")
    creds = Credentials.from_service_account_file(credential_path)
    return build('sheets', 'v4', credentials=creds)

def save_to_gsheet(df, spreadsheet_id, sheet_range, credential_path='google-sheets-api.json'):
    try:
        service = get_gsheet_service(credential_path)
        sheet = service.spreadsheets()

        data = [df.columns.tolist()] + df.values.tolist()
        sheet_name = sheet_range.split('!')[0]

        # Clear existing content
        sheet.values().clear(
            spreadsheetId=spreadsheet_id,
            range=sheet_name
        ).execute()

        # Update with new data
        body = {'values': data}
        result = sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=sheet_range,
            valueInputOption='RAW',
            body=body
        ).execute()

        updated = result.get('updatedCells')
        print(f"[INFO] {updated} cells updated in Google Sheets.")
        return updated
    except Exception as e:
        print(f"[ERROR] Failed to save to Google Sheets: {e}")
        return None
