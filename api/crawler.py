import requests, cfscrape
from bs4 import BeautifulSoup

scraper = cfscrape.create_scraper()
headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

def get_articles():
    articles  =[]
    
    url = "https://www.theblockcrypto.com"
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    article_list = soup.find(class_='w-100')
    article_list_items = article_list.find_all('article')
    for article in article_list_items:
    	base = article.find(class_='border-grey-light')
    	link = base.find(class_='color-outer-space').get('href')
    	title = base.find(class_='color-outer-space').find('h3').get_text()
    	description = base.find(class_='font-body').get_text()

    	data = {'title': title, 'link': url+link, 'description': description}
    	articles.append(data)
        
    return articles

def eth_price():
    url = "https://coingecko.com"
    page = scraper.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    crypto_price = soup.find('tbody')
    eth_price = crypto_price.find('span', {'data-coin-symbol': 'eth'})
    price = eth_price.get_text()

    return price

def address_value(address):
    url = 'https://etherscan.io/address/{}'.format(address)
    page = scraper.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = soup.find(class_='card-body')
    overview = data.find_all(class_='row')
    value = overview[1].find(class_='col-md-8').get_text()

    return value