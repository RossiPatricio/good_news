from scraping import *

cnn= scrap_cnn()
times= scrap_times()
clarin= scrap_clarin()
nbc= scrap_nbc()
tecno= cnn_tecno()
esp= cnn_español()

lista_de_diccionarios = []
def top_news(key_word):
    portals = [cnn, times, clarin, nbc, tecno, esp]
    
    articles= []
    for portal in portals:
        articles.append(portal)

    all_articles=[]
    for element in articles:
        for e in element:
            all_articles.append(e)

    for article in all_articles:
        if key_word in article['title']:
            lista_de_diccionarios.append(article)

    return lista_de_diccionarios
