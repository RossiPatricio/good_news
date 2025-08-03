from scraping import *

info = scrap_infobae()
with open('noticias_infobae.txt', 'w', encoding='utf-8') as f:
    for article in info:
        f.write(f"{article['title']}\n{article['link']}\n{article['image_path']}\n\n")
    print("Infobae")


info = scrap_cnn()
with open('noticias_cnn.txt', 'w', encoding='utf-8') as f:
    for article in info:
        f.write(f"{article['title']}\n{article['link']}\nn")
    print("CNN")


info = scrap_cnn()
with open('noticias_nbc.txt', 'w', encoding='utf-8') as f:
    for article in info:
        f.write(f"{article['title']}\n{article['link']}\nn")
    print("NBC")


info = scrap_cnn()
with open('noticias_times.txt', 'w', encoding='utf-8') as f:
    for article in info:
        f.write(f"{article['title']}\n{article['link']}\nn")
    print("Times")


info = scrap_cnn()
with open('noticias_cbs.txt', 'w', encoding='utf-8') as f:
    for article in info:
        f.write(f"{article['title']}\n{article['link']}\nn")
    print("CBS")


info = scrap_cnn()
with open('noticias_cnnmx.txt', 'w', encoding='utf-8') as f:
    for article in info:
        f.write(f"{article['title']}\n{article['link']}\nn")
    print("CNN MX")

try:
    info = scrap_clarin()
    with open('noticias_clarin.txt', 'w', encoding='utf-8') as f:
        for article in info:
            f.write(f"{article['title']}\n{article['link']}\nn")
        print("Clarin")
except Exception as e:
    print(f'Clarin: Error en la funcion{e}')
