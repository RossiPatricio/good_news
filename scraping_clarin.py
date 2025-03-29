import requests 
from bs4 import BeautifulSoup

def scrap_clarin():
    url = 'https://www.clarin.com/'
    lista_de_diccionarios = []

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    noticia_destacada = soup.find('div', class_='sc-458ac523-0 bvJehW')
    link1 = noticia_destacada.a['href']
    lista_de_diccionarios.append({'title': noticia_destacada.text, 'link': link1, 'portal': 'clarin'})

    content = soup.find_all('div', class_='sc-86b8ec52-0 gPQASe onexone')
    for element in content:
        link = element.a['href']
        lista_de_diccionarios.append({'title': element.text, 'link': link, 'portal': 'clarin'})

    return lista_de_diccionarios
