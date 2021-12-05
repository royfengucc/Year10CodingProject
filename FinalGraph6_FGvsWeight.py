from typing import final
import matplotlib.pyplot as plt
from library import loadList
import pandas as pd
import numpy as np
import statistics as stat
import random
from itertools import cycle



dataPercents = loadList("FinalPercents.csv")
dataHeightsWeights = loadList("FinalHeightsWeights.csv")

masterList = []
dict = {}
graphList = []
for n in range(1, len(dataPercents)):
    p = 1 
    name = dataPercents[n][0]
    if float(dataPercents[n][5]) >= 10 and float(dataPercents[n][11]) >= 50: 
        while p < len(dataHeightsWeights) and name != dataHeightsWeights[p][0]: 
            p += 1

        if p<len(dataHeightsWeights):
            output = float(dataPercents[n][12]) * 100
            playerFTPercent = (f"{output:.2f}")
            playerHeight = dataHeightsWeights[p][1]
            playerWeight = dataHeightsWeights[p][3]
            masterList.append([dataPercents[n][0], playerFTPercent, playerHeight, playerWeight])

for i in range(len(masterList)):
    if masterList[i][3] in dict:
        dict[masterList[i][3]].append(float(masterList[i][1]))
    else:
        dict[masterList[i][3]] = [float(masterList[i][1])]

for key,value in dict.items():
    sum = 0
    average = 0
    for n in value:
        sum += n
    average = sum / len(value)
    finalAverage = round(average, ndigits=1)
    graphList.append([int(key), finalAverage])

graphList.sort()

finalList = []

for i in range(len(graphList)):
    counter = 0
    for j in range(len(masterList)):
        if graphList[i][0] == int(masterList[j][3]): 
            counter += 1
    finalList.append([graphList[i][0], graphList[i][1], (counter * 50)])


df = pd.DataFrame(finalList, columns= ["Weight", "FG", "Counter"])

m, b = np.polyfit(df.FG, df.Weight, 1)
fitEquation = m*df.FG + b

colours = ['y', 'r', 'b', 'o', 'g', 'p']
c = []
for i in range(len(finalList)): 
    c += [random.choice(colours)]

col = (np.random.random(), np.random.random(), np.random.random())

plt.scatter(df.Weight,df.FG, s = df.Counter, c=np.random.rand(len(df.Weight),3), alpha = 0.5)
z = np.polyfit(df.Weight, df.FG, 1)
p = np.poly1d(z)
plt.plot(df.Weight,p(df.Weight),"r--")

plt.yticks(np.arange(0, 105, 5))

legendLabels = ['Trendline', 'Percent for weight']
plt.legend(legendLabels,loc=4)


plt.xlabel('Weight (lbs)', fontweight='bold')
plt.ylabel('FG%', fontweight='bold')
plt.title("Weight VS Field Goal %", fontweight="bold", fontsize=20)

plt.text(222, 92, 'Size of dot represents number of players', bbox={
        'facecolor': 'blue', 'alpha': 0.5, 'pad': 10})

plt.show()



