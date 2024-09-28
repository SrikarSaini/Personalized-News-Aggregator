import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_bbc():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles1 = []
    for item in soup.find_all('div', class_="sc-2448c165-2 eMVRpx"):
        title = item.find('h2').text if item.find('h2') else None
        summary = item.find('p').text if item.find('p') else None
        date = datetime.now().strftime('%Y-%m-%d')
        article_url = item.find('a')['href'] if item.find('a') else None
        if title and article_url:
            articles1.append({
                'title': title,
                'summary': summary,
                'publication_date': date,
                'source': 'BBC',
                'url': f"https://www.bbc.com{article_url}"
            })
    return articles1


def save_to_csv(articles):
    keys = articles[0].keys()
    with open('news_articles.csv', 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(articles)

if __name__ == "__main__":
    bbc_articles = scrape_bbc()
    save_to_csv(bbc_articles)
