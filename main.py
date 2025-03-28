from scraping_infobae import scrap_infobae
from scraping_cnn import *
from scraping_times import *
from scraping_clarin import *
from html_generator import *

scrap_infobae()

cnn = scrap_cnn()
clarin = scrap_clarin()
times = scrap_times() 

portals = [
{'name': 'clarin', 'content':clarin}, 
{'name': 'cnn', 'content':cnn},
{'name': 'times', 'content':times}
]

for portal in portals:
    name= portal['name']
    content= portal['content']
    html_generator(content, name)
