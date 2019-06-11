import numpy as np
import pandas as pd
import io
import codecs
import re
from tqdm import tqdm


""" Cleanning 2_total.stat.v2.0 """


f = io.open("../data/BanglaDataset/2_total.stat.v2.0", mode="r", encoding="utf-8")
sentences = []

for line in f:
    sentences.append(line.split(',')[0])

words = []

# Removing noisy data: Start with kars
invalid_start_word = "ািীুূৃৄেৈোৌৗয়ৎঁঃংঢ়য়ঙঞড়ণ়্৥"
file = codecs.open("removed_data/start_with_kars.txt", "w", "utf-8")
for i, s in enumerate(sentences):
    if s[0] not in invalid_start_word:
        words.append(s)
    else:
        file.write(s + '\n')
        print(s)
        
file.close()          

# Removing noisy data: Double kars
file = codecs.open("removed_data/double_kars.txt", "w", "utf-8")

kars = "ািীুূৃৄেৈোৌ"
new_words = []
for s in words:
    include = True
    for i in range(len(s) - 1):
        if s[i] in kars and s[i+1] in kars:
            include = False
    
    if include:
        new_words.append(s)
    else:
        file.write(s + '\n')
        print(s)
        
file.close()   
words = new_words    


"""Analysis length of the words"""
word_length = []
freq_count = {}

for i in range(len(words)):
    l = len(words[i])
    word_length.append(l)
    
    if l in freq_count.keys():
        freq_count[l] += 1
    else:
        freq_count[l] = 1


new_words = []
removed = 0
file = codecs.open("removed_data/length_gt_20.txt", "w", "utf-8")
for word in words:
    if len(word)>20:
        file.write(word+ '\n')
        removed += 1
    else:
        new_words.append(word)
        
file.close()
print("removed", removed)
words = new_words

word_batch1 = words









""" Cleaning avrodict.txt"""


import json

with open('../data/BanglaDataset/avrodict.js', encoding="utf8") as dataFile:
    data = dataFile.read()
    obj = data[data.find('{') : data.rfind('}')+1]
    
    jsonObj = json.loads(obj)
    
sentences = list(jsonObj.values())
words = []

for line in sentences:
    words.extend(line)





"""Analysis length of the words"""
word_length = []
freq_count = {}

for i in range(len(words)):
    l = len(words[i])
    word_length.append(l)
    
    if l in freq_count.keys():
        freq_count[l] += 1
    else:
        freq_count[l] = 1




# Removing noisy data: Start with kars
new_words = []
file = codecs.open("removed_data_avro/start_with_kars.txt", "w", "utf-8")
for i, s in enumerate(words):
    if s[0] not in invalid_start_word:
        new_words.append(s)
    else:
        file.write(s + '\n')
        print(s)
        
file.close()   
words = new_words     
  

# Removing noisy data: Double kars
file = codecs.open("removed_data_avro/double_kars.txt", "w", "utf-8")

new_words = []
for s in words:
    include = True
    for i in range(len(s) - 1):
        if s[i] in kars and s[i+1] in kars:
            include = False
    
    if include:
        new_words.append(s)
    else:
        file.write(s + '\n')
        print(s)
        
file.close()   
words = new_words  
word_batch2 = words















""" Cleanning  BengaliWordList_439 """


f = io.open("../data/BanglaDataset/BengaliWordList_439.txt", mode="r", encoding="utf-8")
sentences = []

for line in f:
    sentences.append(line)

words = []

# Removing noisy data: Start with kars
file = codecs.open("removed_data_dictwords/start_with_kars.txt", "w", "utf-8")
for i, s in enumerate(sentences):
    if s[0] not in invalid_start_word:
        words.append(s[:-1])
    else:
        file.write(s + '\n')
        print(s)
        
file.close()          


# Removing noisy data: Double kars
file = codecs.open("removed_data_dictwords/double_kars.txt", "w", "utf-8")

new_words = []
for s in words:
    include = True
    for i in range(len(s) - 1):
        if s[i] in kars and s[i+1] in kars:
            include = False
    
    if include:
        new_words.append(s)
    else:
        file.write(s + '\n')
        print(s)
        
file.close()   
words = new_words    


"""Analysis length of the words"""
word_length = []
freq_count = {}

for i in range(len(words)):
    l = len(words[i])
    word_length.append(l)
    
    if l in freq_count.keys():
        freq_count[l] += 1
    else:
        freq_count[l] = 1


new_words = []
removed = 0
file = codecs.open("removed_data_dictwords/length_gt_21.txt", "w", "utf-8")
for word in words:
    if len(word)>21:
        file.write(word+ '\n')
        removed += 1
    else:
        new_words.append(word)
        
file.close()
print("removed", removed)
words = new_words

word_batch3 = words









""" Cleaning ankur-dix.dct """
f = io.open("../data/BanglaDataset/ankur-dix.dct", mode="r", encoding="utf-8")
sentences = []

for line in f:
    sentences.append(line.split(':')[0])

count = 0
for word in sentences:
    if "'" in word:
        print(word)
        count += 1
    
print(count)

words = []
for i in range(len(sentences)):
    words.append(re.sub("'", "", sentences[i]))


"""Analysis length of the words"""
word_length = []
freq_count = {}

for i in range(len(words)):
    l = len(words[i])
    word_length.append(l)
    
    if l in freq_count.keys():
        freq_count[l] += 1
    else:
        freq_count[l] = 1




# Removing noisy data: Start with kars
file = codecs.open("removed_data_ankur/start_with_kars.txt", "w", "utf-8")
for i, s in tqdm(enumerate(words)):
    if len(s)>1:
        if s[0] not in invalid_start_word:
            words.append(s[:-1])
        else:
            file.write(s + '\n')
            print(s)
        
file.close()          


# Removing noisy data: Double kars
file = codecs.open("removed_data_ankur/double_kars.txt", "w", "utf-8")

new_words = []
for s in words:
    include = True
    for i in range(len(s) - 1):
        if s[i] in kars and s[i+1] in kars:
            include = False
    
    if include:
        new_words.append(s)
    else:
        file.write(s + '\n')
        print(s)
        
file.close()   
words = new_words    




word_batch4 = words
    




""" Final marged unique words """
words = word_batch1+word_batch2+word_batch3
words = list(set(words))
words.sort()

file = codecs.open("all_bangla_words.txt", "w", "utf-8")
for word in words:
        file.write(word+ '\n')
    
file.close()


        

        