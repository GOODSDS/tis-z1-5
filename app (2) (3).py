
import requests
from bs4 import BeautifulSoup

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def download_file_from_google_drive(file_id):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    return response.content

def clean_html_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator='\n', strip=True)
    return text[:1000] + "\n\n...[truncated]..."

if __name__ == "__main__":
    file_id = "17q20VTlqaF0TILY8c_0N09JJ-btAOFTv"  # use whichever file you want
    html_content = download_file_from_google_drive(file_id)
    cleaned_text = clean_html_content(html_content)
    print(cleaned_text)
