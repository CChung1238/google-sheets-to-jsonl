import gspread
import re
import json

def clean_text(text):
    """
    Cleans and formats text (removes unnecessary special characters, handles line breaks, etc.).
    """
    text = re.sub(r'[\'\"()\[\]{}]', '', text)  # Removes quotes and brackets
    text = re.sub(r'\s+', ' ', text)    # Converts multiple line breaks/spaces into a single space
    return text.strip()

def format_keywords(keywords):
    """
    Converts line breaks in keywords to commas.

    """
    return keywords.replace('\n', ', ').strip()


def convert_to_jsonl(data, start_row, end_row):
    """
    Converts data into JSONL format.
    """
    jsonl_data = []
    for row in data[start_row-1:end_row]:   # Processes only specified rows
        if len(row) < 3:
            continue                        # Skips rows that are empty or invalid
        keywords = format_keywords(row[0])  # Processes keywords
        title = clean_text(row[1])          # Cleans the title
        content = clean_text(row[2])        # Cleans the content

        # JSONL 형식 생성
        json_entry = {
            "messages": [
                {"role": "system", "content": "You are a blog writer"},
                {"role": "user", "content": f"다음의 내용을 참고해서 블로그를 작성하세요. 블로그 제목:{title}. 키워드:{keywords}"}, # Korean: Refer to the following content and write a blog. Blog title: {title}. Keywords: {keywords}.
                {"role": "assistant", "content": content}
            ]
        }
        jsonl_data.append(json_entry)
    return jsonl_data

def save_as_jsonl(jsonl_data, output_file):
    """
    Saves JSONL data to a file.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for entry in jsonl_data:
            file.write(json.dumps(entry, ensure_ascii=False) + '\n')

def main():
    # Google Sheets API setup
    gc = gspread.service_account(filename='credentials.json')  # Path to the service account JSON file

    # Prompt user for the document key
    document_key = input("Please enter your Google Sheets document key: ")  # User provides the key during runtime
    sh = gc.open_by_key(document_key)  # Google Sheets document key
    worksheet = sh.sheet1  # Selects the first worksheet


    # Fetch data from Google Sheets
    data = worksheet.get_all_values()

    # Specify the range of rows to convert
    start_row = 2  # Example: Start from the 2nd row
    end_row = 31   # Example: End at the 31st row

    # Convert data to JSONL format
    jsonl_data = convert_to_jsonl(data, start_row, end_row)

    # Save JSONL data to a file
    output_file = 'output.jsonl'
    save_as_jsonl(jsonl_data, output_file)
    print(f"JSONL file has been saved to {output_file}.")

if __name__ == '__main__':
    main()
