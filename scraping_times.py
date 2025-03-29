import requests
from bs4 import BeautifulSoup

def scrap_times():
  link = 'https://www.nytimes.com/international/'
  lista_de_diccionarios = []

  response = requests.get(link)
  soup = BeautifulSoup(response.content, 'html.parser')

  elements = soup.find_all('p', class_='indicate-hover css-91bpc3')
  for element in elements:
      titulo = element.get_text().strip()
      enlace_padre = element.find_parent('a')
      if enlace_padre:
          noticia_link = enlace_padre['href']
          lista_de_diccionarios.append({'title': titulo, 'link': noticia_link, 'portal': 'times'})

  return lista_de_diccionarios
