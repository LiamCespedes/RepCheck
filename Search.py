from __future__ import print_function
import plotly
from collections import Counter

import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='lcespedes', api_key='bYprmFWReGrITMUwDoNO')
import io

# import re
# nonascii = bytearray(range(0x80, 0x100))
# with io.open('twitter.txt','r',encoding='ascii',errors='ignore') as infile, \
# io.open('twitter_parsed.txt','w',encoding='ascii',errors='ignore') as outfile:
#  for line in infile:
# outfile.write(bytes.translate(None, nonascii))

nonascii = bytearray(range(0x80, 0x100))
with open('twitter.txt','rb') as infile, open('twitter_parsed.txt','wb') as outfile:
    for line in infile: # b'\n'-separated lines (Linux, OSX, Windows)
        outfile.write(line.translate(None, nonascii))



# data = re.sub(r'[^\x00-\x7f]',r'', str(file))
# print(data)
data = open("twitter_parsed.txt").read().replace('\n', '')

print(data)

positiveWords = []
negativeWords = []

matchedPositives = []
matchedNegatives = []

with open("positive_words.txt") as f:
    for line in f:
        positiveWords.append(line.rstrip())

with open("negative_words.txt") as f:
    for line in f:
        negativeWords.append(line.rstrip())


print(positiveWords)
print(negativeWords)

data1 = data.split(" ")
i = 0
for x in data1:
    for j in positiveWords:
        if x == j:
            i += 1
            matchedPositives.append(x)

print("Positive word count is " + str(i))

data2 = data.split(" ")
c = 0
for x in data2:
    for j in negativeWords:
        if x == j:
            c += 1
            matchedNegatives.append(x)
print("Negative word count is " + str(c))

print("Positives Matched: " + str(matchedPositives))
print("Negatives Matched: " + str(matchedNegatives))

matchedPositivesFreq = Counter(matchedPositives)
print(matchedPositivesFreq)
matchedNegativesFreq = Counter(matchedNegatives)
print(matchedNegativesFreq)

posWordlabels = []
posWordvalues = []

for x in matchedPositivesFreq:
    if matchedPositivesFreq[x] != 1:
        posWordlabels.append(x)
        posWordvalues.append(matchedPositivesFreq[x])
    else:
        pass



positiveWordChart = go.Pie(labels=posWordlabels, values=posWordvalues)

negWordlabels = []
negWordvalues = []

for x in matchedNegativesFreq:
    if matchedNegativesFreq[x] != 1:
        negWordlabels.append(x)
        negWordvalues.append(matchedNegativesFreq[x])
    else:
        pass

print(str(posWordlabels))
print(str(posWordvalues))

negativeWordChart = go.Pie(labels=negWordlabels, values=negWordvalues)

py.iplot([positiveWordChart], filename='basic_pie_chart')
py.iplot([negativeWordChart], filename='basic_pie_chart')
# for lines in twitterData:
#    thing = twitterData[lines]
#    print(thing)
# words = ['doctor', 'man']
# s = 'the man is a doctor, the doctor is a man, doctor, man, doctor'

# labels = ['Positive Reception', 'Negative Reception']
# values = [i, c]
# trace = go.Pie(labels=labels, values=values)

# py.iplot([trace], filename='basic_pie_chart')

