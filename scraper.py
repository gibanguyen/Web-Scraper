import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_content(url):
    """
    Fetch the content of the URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the content: {e}")
        return None

def parse_content(html_content):
    """
    Parse the HTML content and extract data.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []
    
    # Example: Extract all links
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.text.strip()
        data.append({'text': text, 'href': href})
    
    return data

def save_data(data, filename='data.csv'):
    """
    Save the extracted data to a CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description='Web scraper tool')
    parser.add_argument('url', type=str, help='The URL to scrape')
    parser.add_argument('filename', type=str, help='The filename to save the data (e.g., data.csv)')
    
    args = parser.parse_args()
    print(args)
    
    html_content = fetch_content(args.url)
    if html_content:
        data = parse_content(html_content)
        save_data(data, args.filename)

if __name__ == "__main__":
    main()
