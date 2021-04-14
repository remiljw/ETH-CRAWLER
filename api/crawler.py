import requests
from bs4 import BeautifulSoup

def get_articles():
    articles  =[]
    
    url = "https://www.theblockcrypto.com"
    page = requests.get(url)
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
    pass