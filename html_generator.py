def html_generator(article, portal):
    file = f'C:\\Users\\PRossi\\code\\good-news\\templates\\{portal}.html'

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NYT</title>
    </head>
    <body>
        <main>
            <h1>NEWS</h1>
            <hr>
            {article_content}
        </main>
    </body>
    </html>
    """

    article_template = """
    <div class="article">
        <h2><a href="{link}" target="_blank">{title}</a></h2>
    </div>
    """

    articles_html = ''.join([article_template.format(title=articl['title'], link=articl['link']) for articl in article])

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html_template.format(article_content=articles_html))

    print(f"Proceso completado: {portal}")
