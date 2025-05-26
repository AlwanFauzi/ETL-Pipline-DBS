import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def save_to_csv(df, filename='products.csv'):
    df.to_csv(filename, index=False)
    print(f"[INFO] Saved to {filename}")

def save_to_gsheet(df, spreadsheet_id, sheet_range):
    creds = Credentials.from_service_account_file('google-sheets-api.json')
    service = build('sheets', 'v4', credentials=creds)
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

    print(f"[INFO] {result.get('updatedCells')} cells updated in Google Sheets.")
