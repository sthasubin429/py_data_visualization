import numpy as np
import matplotlib.pyplot as plt

f = open("lyrics.txt", "r")
temp = f.read().lower().split()
wordList = []
for word in temp:
    if "-" in word:
        subWord = word.split('-')
        for w in subWord:
            wordList.append(w.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\""))
    else:
        wordList.append(word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\""))
f.close()
print(wordList)

uniqueWords = []
for i in wordList:
    if i not in uniqueWords:
        uniqueWords.append(i)
print(uniqueWords)
a = np.linspace(255, 1, len(uniqueWords), dtype=int)

colorDict = {}
for i in range(0, len(uniqueWords)):
    colorDict[uniqueWords[i]] = a[i]

img = []
for i in wordList:
    row = []
    for j in wordList:
        if i == j:
            row.append(colorDict[j])
        else:
            row.append(0)
    img.append(row)
fig = plt.figure(figsize=(20, 20))
plt.imshow(img, interpolation='nearest', aspect='auto')

fig.savefig('plot.png')
