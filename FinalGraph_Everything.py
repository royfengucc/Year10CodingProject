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

col = {
    "FT":10,
    "FG": 12,
    "3PT": 14
}


def getMasterList(): 
    for n in range(1, len(dataPercents)):
        p = 1 
        name = dataPercents[n][0]
        if float(dataPercents[n][5]) >= 10 and float(dataPercents[n][9]) >= 50: 
            while p < len(dataHeightsWeights) and name != dataHeightsWeights[p][0]: 
                p += 1

            if p<len(dataHeightsWeights):
                output = float(dataPercents[n][10]) * 100
                playerShootingPercent = (f"{output:.2f}")
                playerHeight = dataHeightsWeights[p][1]
                playerWeight = dataHeightsWeights[p][3]
                masterList.append([dataPercents[n][0], playerShootingPercent, playerHeight, playerWeight])
