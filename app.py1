
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

# Use one of the uploaded Google Drive files
if __name__ == "__main__":
    file_id = "17q20VTlqaF0TILY8c_0N09JJ-btAOFTv"  # You can swap this with the other file ID if needed
    cleaned_text = download_and_clean_html(file_id)
    print(cleaned_text)
