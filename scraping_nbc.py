import requests
from bs4 import BeautifulSoup

def scrape_nbc():
    url = 'https://www.nbcnews.com/latest-stories/'
    url2 = 'https://www.nbcnews.com/'
    lista_de_diccionarios = []

    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    news_1 = soup2.find_all('h2', class_='multistoryline__headline founders-cond fw6 lead')
    for element in news_1:
        titulo2= element.text
        link2= element.a['href']
        lista_de_diccionarios.append({'title': titulo2, 'link': link2, 'portal': 'nbc'})  

    news_2 = soup2.find_all('h2', class_='storyline__headline founders-cond fw6 large')
    for element in news_2:
        titulo2= element.text
        link2= element.a['href']
        lista_de_diccionarios.append({'title': titulo2, 'link': link2, 'portal': 'nbc'})

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find_all('h2', class_='multistoryline__headline founders-cond fw6 large noBottomSpace')
    for element in content:
        titulo= element.text
        link= element.a['href']
        lista_de_diccionarios.append({'title': titulo, 'link': link, 'portal': 'nbc'})  

    return lista_de_diccionarios
