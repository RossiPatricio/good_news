from scraping import *
from html_generator import *
from top_news import top_news

scrapers = {
    "cnn": scrap_cnn(),
    "clarin": scrap_clarin(),
    "times": scrap_times(),
    "cnn_esp": cnn_español(),
    "nbc": scrap_nbc(),
    "cbs": scrap_cbs(),
    "infobae": scrap_infobae(),
}

keys= [
    'Francisco','Messi','2026','programming','movie','Putin', 'Nirvana', 'Michael Jackson',
    'Milei', 'nvidia', 'Quilmes', 'Oasis', 'Zelensky', 'Kirchner', 'Musk', 'Burton', 'Cobain',
    'Ukraine','Potter', 'Rowling', 'Webb', 'SpaceX', 'NASA', 'Depp', 'Ucrania', 'Poe', 'chess', 
    'Magnus Carlsen', 'argentino', 'Argentina', 'Argentinian', 'tim burton', 'gothic', 'church',
    'jesus', 'yisus', 'ia', 'programming', 'python', 'skateboarding', 'skate', 'inteligencia artifical',
    'artificial intelligence', 'specie', 'species', 'Egypt', 'discovery', 'death', 'died', 'die',
    '2026 world cup', 'war', 'openai', 'chatgpt', 'deepseek', 'grok', 'ia china', 'rowling','harry potter',
    'daniel radcliffe', 'rupert grint', 'emma watson', 'harry potter hbo', 'harry potter series']


for portals, scraper in scrapers.items():
    try:
        content = scraper
    except:
        continue
    name = portals
    html_generator(content, name)

for key in keys:    
    top = top_news(key)
