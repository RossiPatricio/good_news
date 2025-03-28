import requests
from bs4 import BeautifulSoup

def scrape_nbc():
    url = 'https://www.nbcnews.com/latest-stories/'
    url2 = 'https://www.nbcnews.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    lista_de_diccionarios = []

    # 2 PRINCIPALES
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    first = soup2.find_all('h2', class_='multistoryline__headline founders-cond fw6 lead')
    for element in first:
        titulo2= element.text
        link2= element.a['href']
        lista_de_diccionarios.append({'Title: ': titulo2, 'Link: ': link2})  

    # 2 MAS RECIENTES
    content = soup.find_all('h2', class_='multistoryline__headline founders-cond fw6 large noBottomSpace')
    for element in content:
        titulo= element.text
        link= element.a['href']
        lista_de_diccionarios.append({'Title: ': titulo, 'Link: ': link})  

    # PRINCIPALES
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    first = soup2.find_all('h2', class_='storyline__headline founders-cond fw6 large')
    for element in first:
        titulo2= element.text
        link2= element.a['href']
        lista_de_diccionarios.append({'Title: ': titulo2, 'Link: ': link2})

    return lista_de_diccionarios
