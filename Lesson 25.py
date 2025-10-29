import requests
from bs4 import BeautifulSoup

for page in range(1, 51):
    print(f"\n--- Сторінка {page} ---")
    
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        print(f"{title}: {price}")
 