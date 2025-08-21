from scraping import *

portals = [
    {
        'name' : 'Infobae',
        'file': 'noticias_infobae.txt',
        'articles': scrap_infobae()
    },
    {
        'name' : 'CNN',
        'file': 'noticias_cnn.txt',
        'articles': scrap_cnn()
    },
    {
        'name' : 'New York Times',
        'file': 'noticias_times.txt',
        'articles': scrap_times()
    },
    {
        'name' : 'CBS',
        'file': 'noticias_cbs.txt',
        'articles': scrap_cbs()
    },
    {
        'name' : 'NBC',
        'file': 'noticias_nbc.txt',
        'articles': scrap_nbc()
    },
    {
        'name' : 'CNN Español',
        'file': 'noticias_cnnmx.txt',
        'articles': cnn_español()
    },
    {
        'name' : 'Clarin',
        'file': 'noticias_clarin.txt',
        'articles': scrap_clarin()
    },
]


for portal in portals:
    try:
        info = portal['articles']
        with open(portal['file'], 'w', encoding='utf-8') as f:
            for article in info:
                f.write(f"{article['title']}\n{article['link']}\n\n")
            print(f"Terminado: {portal['name']}")
    except Exception as e:
        print(f"Error: {e}")

