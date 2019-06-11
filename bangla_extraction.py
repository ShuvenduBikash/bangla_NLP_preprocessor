import re
import codecs

lines = ""
with codecs.open("viqw.html", mode='r', encoding='utf-8') as f:
    for line in f:
        lines += line
        
bangla_line = re.sub("[^\\u0980-\\u09FF\n।\-_, ]+", " ", lines)

bangla_line = re.sub(", | ,", " ", bangla_line)
bangla_line = re.sub("[' ']+", " ", bangla_line)

bangla_line = bangla_line.split("\n")

cleanned_text =[]
for line in bangla_line:
    if len(line) > 10:
        cleanned_text.append(line)

with codecs.open("cleanned_lines.txt", mode="a", encoding="utf-8") as f:
    for line in cleanned_text:
        f.writelines(line+'\n')