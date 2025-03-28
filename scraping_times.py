import requests
from bs4 import BeautifulSoup

archivo = r'C:\Users\PRossi\Desktop\news\times.txt'
archivo2 = r'C:\Users\PRossi\code\scraping-news\templates\times.html'

def scrap_times():
    link = 'https://www.nytimes.com/international/'
    archivo = r'C:\Users\PRossi\Desktop\news\times.txt'
    dic= {}

    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')

    elements = soup.find_all('p', class_='indicate-hover css-91bpc3')
    for element in elements:
        titulo = element.get_text().strip()
        enlace_padre = element.find_parent('a')
        if enlace_padre:
            noticia_link = enlace_padre['href']
            dic[titulo] = noticia_link

    with open(archivo, 'w') as file:
        for a,b in dic.items():
            file.write(f'Title: {a}\nLink: {b}\n\n')

    # Convertir el diccionario en una lista de artículos
    articles = [{'title': key, 'link': value} for key, value in dic.items()]
    return articles  # Se retorna la lista de artículos

# Extraer artículos
articles = scrap_times()

# Plantilla HTML principal con un marcador para el contenido de los artículos
html_template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NYT</title>
  </head>
  <body>
    <main>
        <h1>THE NEW YORK TIMES</h1>
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