import requests
from bs4 import BeautifulSoup

archivo = r'C:\Users\PRossi\code\cnn.txt'
archivo2 = r'C:\Users\PRossi\code\scraping-news\templates\cnn_news.html'

def scrap_cnn():
    url = 'https://edition.cnn.com/'
    dic = {}

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    content = soup.find('h2', class_='container__title_url-text container_lead-plus-headlines-with-images__title_url-text')
    if content:
        titulo = content.text.strip()
        enlace_padre = content.find_parent('a')
        if enlace_padre:
            image_link = url + enlace_padre['href']
            dic[titulo] = image_link

    content1 = soup.find_all('div', class_='container__text container_lead-plus-headlines-with-images__text')
    for e in content1:
        titulo = e.text.strip()
        enlace_padre = e.find_parent('a')
        if enlace_padre:
            image_link = url + enlace_padre['href']
            dic[titulo] = image_link

    with open(archivo, 'w', encoding='utf-8') as file:
        for a, b in dic.items():
            file.write(f'Title: {a}\nLink: {b}\n\n')

    # Convertir el diccionario en una lista de artículos
    articles = [{'title': key, 'link': value} for key, value in dic.items()]
    return articles  # Se retorna la lista de artículos

# Extraer artículos
articles = scrap_cnn()

# Plantilla HTML principal con un marcador para el contenido de los artículos
html_template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CNN</title>
  </head>
  <body>
    <main>
        <h1>CNN NEWS</h1>
        <hr>
        {articles_content}
    </main>
  </body>
</html>
"""

# Plantilla para cada artículo
article_template = """
<div class="article">
    <h2><a href="{link}" target="_blank">{title}</a></h2>
</div>
"""

# Generar el HTML de los artículos
articles_html = ''.join([article_template.format(title=article['title'], link=article['link']) for article in articles])

# Integrar el contenido de los artículos en la plantilla HTML principal
html_final = html_template.format(articles_content=articles_html)

# Guardar el HTML final en un archivo
with open(archivo2, "w", encoding="utf-8") as f:
    f.write(html_final)

print("HTML generado y guardado.")
