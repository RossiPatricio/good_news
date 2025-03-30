from scraping import *
from html_generator import *
from top_news import top_news

info = scrap_infobae()
cnn = scrap_cnn()
clarin = scrap_clarin()
times = scrap_times()
nbc= scrap_nbc() 
cnn_esp= cnn_español()
cbs= scrap_cbs()

keys= ['Francisco','Messi','2026','programming','movie','Putin', 'Nirvana', 'Michael Jackson',
       'Milei', 'nvidia', 'Quilmes', 'Oasis', 'Zelensky', 'Kirchner', 'Musk', 'Burton', 'Cobain',
       'Ukraine','Potter', 'Rowling', 'Webb', 'SpaceX', 'NASA', 'Depp', 'Ucrania', 'Poe']

for key in keys:    
    top = top_news(key)

portals = [
{'name': 'cnn', 'content':cnn},
{'name': 'times', 'content':times},
{'name': 'nbc', 'content':nbc},
{'name': 'cnn_esp', 'content':cnn_esp},
{'name': 'top', 'content':top},
{'name': 'cbs', 'content':cbs},
{'name': 'infobae', 'content':info},
]

for portal in portals:
    name= portal['name']
    content= portal['content']
    html_generator(content, name)
