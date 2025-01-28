# Google Sheets to JSONL Converter
This Python script converts Google Sheets data into a JSONL format, specifically designed for OpenAI fine-tuning purposes.

## Features
- Reads data from Google Sheets using the Google Sheets API.
- Cleans and formats text (removes unnecessary special characters, handles line breaks, etc.).
- Outputs data in JSONL format, ready for OpenAI fine-tuning.

## Requirements
- Python 3.x
- Libraries: `gspread`, `oauth2client`

## How to Use
1. Clone this repository:
   git clone https://github.com/cchung1238/google-sheets-to-jsonl.git
2. Install dependencies:
   pip install -r requirements.txt
3. Place your Google Sheets API credentials (`credentials.json`) in the project directory.
4. Run the script:
   python fileConverter.py
5. Enter your Google Sheets document ID.
   The script will prompt you to enter your Google Sheets document ID.

## Sample Output
```jsonl
{"messages":[{"role":"system","content":"You are a blog writer"},{"role":"user","content":"다음의 내용을 참고해서 블로그를 작성하세요. 블로그 제목:Example Title. 키워드:Example Keywords."},{"role":"assistant","content":"Example content"}]}
