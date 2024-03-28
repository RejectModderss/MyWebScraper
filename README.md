# MyWebScraper

MyWebScraper is a Python-based web scraper that extracts both text and CSS data from a webpage and saves them into separate files.

## How It Works

1. **Initialization**: The `MyWebScraper` class is initialized with a URL of the webpage you want to scrape.

2. **Fetching HTML**: The `fetch_html` method sends a GET request to the provided URL and returns the HTML content of the webpage.

3. **Parsing HTML**: The `parse_html` method uses BeautifulSoup to parse the fetched HTML and returns a BeautifulSoup object.

4. **Extracting Data**: The `extract_data` method iterates over all tags in the BeautifulSoup object. If a tag is a `<style>` tag or a `<link>` tag with `rel="stylesheet"`, it's considered as CSS and added to the `css_data` list. If a tag has a string (i.e., it's not a container tag like `<div>` or `<span>`), it's considered as text and added to the `text_data` list.

5. **Outputting Data**: The `output_data` method writes the extracted data into a file. It's called twice in the `run` method to output the text and CSS data to 'text_data.txt' and 'css_data.txt' respectively.

## Requirements

This project requires Python 3 and the following Python packages:

- requests
- beautifulsoup4

You can install these packages using pip:

```bash
pip install -r requirements.txt
