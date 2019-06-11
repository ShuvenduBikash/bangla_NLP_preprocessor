import newspaper
import re
import codecs

lines = ""
with codecs.open("ptwx.html", mode='r', encoding='utf-8') as f:
    for line in f:
        lines += line

article = newspaper.Article(url='', language='bn') 
article.set_html(lines)  # article.download()
article.parse()



print(article.title)
print(article.text)
