# Web Scraper Tool

This project is a simple web scraping tool built using Python. The tool fetches content from a specified URL, parses the HTML to extract data, and saves the data into a CSV file.

## Features

- Fetch HTML content from a given URL
- Parse the HTML to extract all hyperlinks
- Save extracted data to a CSV file
- Command-line interface for easy usage

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/gibanguyen/Web-Scraper.git
   cd Web-Scraper
   ```

2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

## Usage

Run the script with the URL to scrape and the filename to save the data:

```bash
python scraper.py <URL> <filename.csv>
```

Example:

```bash
python scraper.py http://example.com data.csv
```

## Code Overview

`scraper.py` This script contains the main logic for the web scraper.

- `fetch_content(url)`: Fetches the HTML content of the URL.
- `parse_content(html_content)`: Parses the HTML content and extracts data.
- `save_data(data, filename)`: Saves the extracted data to a CSV file.
- `main()`: Handles command-line arguments and orchestrates the scraping process.
