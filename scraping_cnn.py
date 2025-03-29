import requests
from bs4 import BeautifulSoup

def scrap_cnn():
    url = 'https://edition.cnn.com/'
    lista_de_diccionarios = []

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    content = soup.find('h2', class_='container__title_url-text container_lead-plus-headlines-with-images__title_url-text')
    if content:
        titulo = content.text.strip()
        enlace_padre = content.find_parent('a')
        if enlace_padre:
            link = url + enlace_padre['href']
            lista_de_diccionarios.append({'title': titulo, 'link': link, 'portal': 'cnn'})

    content1 = soup.find_all('div', class_='container__text container_lead-plus-headlines-with-images__text')
    for e in content1:
        titulo = e.text.strip()
        enlace_padre = e.find_parent('a')
        if enlace_padre:
            link = url + enlace_padre['href']
            lista_de_diccionarios.append({'title': titulo, 'link': link, 'portal': 'cnn'})

    return lista_de_diccionarios
