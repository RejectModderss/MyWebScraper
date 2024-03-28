import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        response = requests.get(self.url)
        return response.text

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def extract_data(self, soup):
        pass

    def output_data(self, data, filename):
        with open(filename, 'w') as file:
            for row in data:
                file.write(' '.join(row) + '\n')

    def run(self):
        html = self.fetch_html()
        soup = self.parse_html(html)
        data = self.extract_data(soup)

class MyWebScraper(WebScraper):
    def __init__(self, url):
        super().__init__(url)

    def extract_data(self, soup):
        text_data = []
        css_data = []
        for tag in soup.find_all(True):
            if tag.name == 'style':
                css_data.append(['style', tag.string if tag.string else ''])
            elif tag.name == 'link' and tag.get('rel') == ['stylesheet']:
                if 'href' in tag.attrs:
                    css_url = tag['href']
                    if 'http' not in css_url:
                        if css_url.startswith('/'):
                            css_url = self.url + css_url
                        else:
                            css_url = self.url + '/' + css_url
                    try:
                        response = requests.get(css_url)
                        css_data.append(['link', response.text])
                    except requests.exceptions.RequestException:
                        css_data.append(['link', 'Failed to fetch CSS from ' + css_url])
            elif tag.string:
                text_data.append([tag.name, tag.string])
        return text_data, css_data

    def run(self):
        html = self.fetch_html()
        soup = self.parse_html(html)
        text_data, css_data = self.extract_data(soup)
        self.output_data(text_data, 'text_data.txt')
        self.output_data(css_data, 'css_data.txt')


def main():
    def start_scraping():
        url = url_entry.get()
        scraper = MyWebScraper(url)
        scraper.run()

    root = tk.Tk()

    window_width = 200
    window_height = 100

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    url_entry = tk.Entry(root)
    url_entry.pack()
    start_button = tk.Button(root, text="Start Scraping", command=start_scraping)
    start_button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()