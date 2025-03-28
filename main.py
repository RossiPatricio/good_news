from scraping_cnn import *
from scraping_times import *
from scraping_clarin import *
from scraping_nbc import *
from scraping_infobae import *
from html_generator import *

scrap_infobae()
cnn = scrap_cnn()
clarin = scrap_clarin()
times = scrap_times() 
nbc = scrape_nbc()

portals = [
{'name': 'clarin', 'content':clarin}, 
{'name': 'cnn', 'content':cnn},
{'name': 'times', 'content':times},
{'name': 'nbc', 'content':nbc},
]

for portal in portals:
    name= portal['name']
    content= portal['content']
    html_generator(content, name)
