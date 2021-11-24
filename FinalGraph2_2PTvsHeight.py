import random
from typing import Counter
import matplotlib.pyplot as plt
from library import loadList
import pandas as pd
import numpy as np
import statistics as stat

dataPercents = loadList("FinalPercents.csv")
dataHeightsWeights = loadList("FinalHeightsWeights.csv")

masterList = []
dict = {}

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
    if masterList[i][2] in dict:
        dict[masterList[i][2]].append(float(masterList[i][1]))
    else:
        dict[masterList[i][2]] = [float(masterList[i][1])]

biglist = []
keyList = []
averageList = []

graphList = []


for key,value in dict.items():
    sum = 0
    average = 0
    for n in value:
        sum += n
    average = sum / len(value)
    finalAverage = round(average, ndigits=2)
    graphList.append([int(key), finalAverage])

graphList.sort()

df = pd.DataFrame(graphList, columns= ["Height", "FT"])

average = stat.mean(df.FT)


m, b = np.polyfit(df.Height, df.FT, 1)
fitEquation = m*df.Height + b




plt.xlabel('Height (inches)', fontweight='bold')
plt.ylabel('FG%', fontweight='bold')
plt.title("Height VS Field Goal (2PT)%", fontweight="bold", fontsize=20)

plt.bar(df.Height, df.FT)
plt.xticks(np.arange(69, 87, 1.0))
plt.yticks(np.arange(0, 105, 5))
plt.plot(df.Height, fitEquation, "--",color = "red")
plt.axhline(y = average,linewidth = 1,color = "gray")
plt.xticks(np.arange(69, 87, 1.0))
plt.yticks(np.arange(0, 105, 5))

legendLabels = ['Trendline','Average FT%',"FT% for height"]
plt.legend(legendLabels,loc=1)

plt.show()



