from scraping_infobae import scrap_infobae
from scraping import *
from html_generator import *
from top_news import top_news

scrap_infobae()
cnn = scrap_cnn()
clarin = scrap_clarin()
times = scrap_times()
nbc= scrap_nbc() 
cnn_esp= cnn_español()
cnn_tec= cnn_tecno()

keys= ['Trump','world','Argentina','fmi','Francisco','Messi','2026','programming','movie','Putin',
       'Milei','argentino', 'nvidia', 'quilmes', 'Oasis', 'Zelensky', 'Kirchner', 'Musk', 'Burton'
       'Ukraine','Potter', 'Rowling', 'Webb', 'SpaceX', 'NASA']

for key in keys:    
    top = top_news(key)

portals = [
{'name': 'cnn', 'content':cnn},
{'name': 'times', 'content':times},
{'name': 'nbc', 'content':nbc},
{'name': 'cnn_tecno', 'content':cnn_tec},
{'name': 'cnn_esp', 'content':cnn_esp},
{'name': 'top', 'content':top},
]

for portal in portals:
    name= portal['name']
    content= portal['content']
    html_generator(content, name)
