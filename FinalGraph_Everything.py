import random
from typing import Counter
import matplotlib.pyplot as plt
from library import loadList
import pandas as pd
import numpy as np
import statistics as stat

dataPercents = loadList("FinalPercents.csv")
dataHeightsWeights = loadList("FinalHeightsWeights.csv")

dict = {}

col = {
    "FT":[10, 'masterListFT'],
    "FG": [12, 'masterListFG'],
    "3PT": [14, 'masterList3PT']
}

def getMasterList(index, L):
    global col 
    for n in range(1, len(dataPercents)):
        p = 1 
        name = dataPercents[n][0]
        if float(dataPercents[n][5]) >= 10 and float(dataPercents[n][index - 1]) >= 50: 
            while p < len(dataHeightsWeights) and name != dataHeightsWeights[p][0]: 
                p += 1

            if p<len(dataHeightsWeights):
                output = float(dataPercents[n][index]) * 100
                playerShootingPercent = (f"{output:.2f}")
                playerHeight = dataHeightsWeights[p][1]
                playerWeight = dataHeightsWeights[p][3]
                L.append([dataPercents[n][0], playerShootingPercent, playerHeight, playerWeight])
    
    dictL = {}
    for i in range(len(L)):
        if L[i][2] in dictL:
            dictL[L[i][2]].append(float(L[i][1]))
        else:
            dictL[L[i][2]] = [float(L[i][1])]
    
    biglist = []
    keyList = []
    averageList = []

    graphList = []

    for key,value in dictL.items():
        sum = 0
        average = 0
        for n in value:
            sum += n
        average = sum / len(value)
        finalAverage = round(average, ndigits=2)
        graphList.append([int(key), finalAverage])

    graphList.sort()

    return graphList

masterListFT = getMasterList(col['FT'][0], [])
masterListFG = getMasterList(col['FG'][0], [])
masterList3PT = getMasterList(col['3PT'][0], [])

masterListFT.sort()
masterListFG.sort()
masterList3PT.sort()

#graphing: 
#----------------------------------------------------------------------------------------------------------------

dfFT = pd.DataFrame(masterListFT, columns= ["Height", "FT"])
dfFG = pd.DataFrame(masterListFG, columns= ["Height", "FG"])
df3PT = pd.DataFrame(masterList3PT, columns= ["Height", "THREE"])

m, b = np.polyfit(dfFT.Height, dfFT.FT, 1)
fitEquationFT = m*dfFT.Height + b

m, b = np.polyfit(dfFG.Height, dfFG.FG, 1)
fitEquationFG = m*dfFG.Height + b

m, b = np.polyfit(df3PT.Height, df3PT.THREE, 1)
fitEquation3PT = m*df3PT.Height + b

plt.scatter(dfFT.Height, dfFT.FT)
plt.plot(dfFT.Height, dfFT.FT, "b")
plt.plot(dfFT.Height, fitEquationFT, "--",color = "red")

plt.scatter(dfFG.Height, dfFG.FG)
plt.plot(dfFG.Height, dfFG.FG, "y")
plt.plot(dfFG.Height, fitEquationFG, "--",color = "red")

plt.scatter(df3PT.Height, df3PT.THREE)
plt.plot(df3PT.Height, df3PT.THREE, "g")
plt.plot(df3PT.Height, fitEquation3PT, "--",color = "red")

plt.xticks(np.arange(69, 87, 1.0))
plt.yticks(np.arange(0, 105, 5))

plt.xlabel('Height (inches)', fontweight='bold')
plt.ylabel('Percentage (%)', fontweight='bold')
plt.title("Height VS Shooting Percentage %", fontweight="bold", fontsize=20)
plt.show()

