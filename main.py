
import requests
from bs4 import BeautifulSoup

def download_and_clean_html(drive_file_id):
    # Construct the direct download URL
    url = f"https://drive.google.com/uc?export=download&id={drive_file_id}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return f"Failed to download file: {response.status_code}"

    # Parse HTML and extract clean text
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text(separator='\n', strip=True)
    
    # Limit output for preview
    return text[:1000] + "\n\n...[truncated]..."

# Example usage
if __name__ == "__main__":
    file_id = "PASTE_YOUR_FILE_ID_HERE"
    cleaned_text = download_and_clean_html(file_id)
    print(cleaned_text)
