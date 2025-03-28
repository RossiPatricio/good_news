import requests
from bs4 import BeautifulSoup

archivo = r'C:\Users\PRossi\Desktop\news\infobae.txt'
archivo2 = r'C:\Users\PRossi\code\scraping-news\templates\infobae.html'

def scrap_infobae():
    url = 'https://www.infobae.com'
    articles = []  # Lista para almacenar los artículos
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscar elementos h2 con la clase indicada
    elements = soup.find_all('h2', class_='story-card-hl headline-link')
    for e in elements:
        title = e.text.strip()
        enlace_padre = e.find_parent('a')
        if enlace_padre:
            href = enlace_padre.get('href', '')
            # Si el href no es absoluto, concatenamos la URL base
            if not href.startswith('http'):
                article_link = url + href
            else:
                article_link = href
            image = enlace_padre.find('img', class_='global-image story-card-img')
            if image:
                image_url = image.get('src', 'No image found')
            else:
                image_url = 'No image found'
            articles.append({'title': title, 'link': article_link, 'image_url': image_url})
    
    # Guardar resultados en un archivo de texto
    with open(archivo, 'w', encoding='utf-8') as file:
        for article in articles:
            file.write(f'Titulo: {article["title"]}\nLink: {article["link"]}\nImagen: {article["image_url"]}\n\n')
    
    return articles

# Extraer artículos
articles = scrap_infobae()

# Plantilla HTML principal
html_template = """
<html>
<head>
    <title>INFOBAE</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>INFOBAE</h1>
    <hr>

    <div id="articles">
        {articles}
    </div>
</body>
</html>
"""

# Plantilla para cada artículo
article_template = """
<div class="article">
    <h2><a href="{link}">{title}</a></h2>
    <img src="{image_url}" alt="Miniatura" width="200">
</div>
"""

# Generar el contenido HTML para los artículos
articles_html = ''.join([article_template.format(title=article['title'], link=article['link'], image_url=article['image_url']) for article in articles])

# Escribir el archivo HTML
with open(archivo2, 'w', encoding='utf-8') as f:
    f.write(html_template.format(articles=articles_html))

print("Proceso completado: Archivo articles.html generado.")
