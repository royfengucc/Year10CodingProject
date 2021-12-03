import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from library import loadList
import random
import pandas as pd

dataPercents = loadList("FinalPercents.csv")
dataHeightsWeights = loadList("FinalHeightsWeights.csv")

dict = {}

col = {
    "FT":[10, 'masterListFT'],
    "FG": [12, 'masterListFG'],
    "3PT": [14, 'masterList3PT'], 
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

dfFT = pd.DataFrame(masterListFT, columns= ["Height", "FT"])
dfFG = pd.DataFrame(masterListFG, columns= ["Height", "FG"])
df3PT = pd.DataFrame(masterList3PT, columns= ["Height", "THREE"])
colours = ['y', 'r', 'b', 'o', 'g', 'p']
c = []


for i in range(len(finalList)): 
    c += [random.choice(colours)]

col = (np.random.random(), np.random.random(), np.random.random())

plt.scatter(df.Weight,df.FT, s = df.Counter, c=np.random.rand(len(df.Weight),3), alpha = 0.5)

t = np.arange(0.0, 2.0, 0.01)
s0 = plt.scatter(df.Weight,df.FT, s = df.Counter, c=np.random.rand(len(df.Weight),3), alpha = 0.5)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)

fig, ax = plt.subplots()
l, = ax.plot(t, s0, lw=2, color='red')
plt.subplots_adjust(left=0.3)

axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('2 Hz', '4 Hz', '8 Hz'))


# def hzfunc(label):
#     hzdict = {'2 Hz': s0, '4 Hz': s1, '8 Hz': s2}
#     ydata = hzdict[label]
#     l.set_ydata(ydata)
#     plt.draw()
# radio.on_clicked(hzfunc)

# plt.show()