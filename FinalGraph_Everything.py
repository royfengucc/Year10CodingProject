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
print('this is ft')
for i in masterListFT: 
    print(i)
print('this is fg')
for i in masterListFG: 
    print(i)
print('this is 3pt')
for i in masterList3PT: 
    print(i)