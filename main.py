from scraping_cnn import *
from scraping_times import *
from scraping_clarin import *
from scraping_nbc import *
from html_generator import *
from top_news import top_news

cnn = scrap_cnn()
clarin = scrap_clarin()
times = scrap_times()
nbc= scrape_nbc() 

keys= ['Trump','world','Argentina','fmi']
for key in keys:    
    top = top_news(key)

portals = [
{'name': 'clarin', 'content':clarin}, 
{'name': 'cnn', 'content':cnn},
{'name': 'times', 'content':times},
{'name': 'nbc', 'content':nbc},
{'name': 'top', 'content':top},
]

for portal in portals:
    name= portal['name']
    content= portal['content']
    html_generator(content, name)
