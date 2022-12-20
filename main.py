import pandas as pd
import sqlalchemy as db
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import os
import math

#Erster Test
print('Diese Lösung wurde mit folgenden Versionen erstellt:')
print('sqlalchemy: ', db.__version__)
print('pandas: ', pd.__version__)
#print('matplotlib: ', plt.__version__)

#Abruf Laufwerkspfad
pfad = os.path.dirname(__file__)
print ("Verwendeter Laufwerkspfad:", pfad)

#Einlesen der Dateien
ideal = pd.read_csv("/Users/micha/Documents/GitHub/DLMDWPMP01---Programmieren-mit-Python/ideal.csv")
ideal.set_index('x',inplace=True)
training = pd.read_csv("/Users/micha/Documents/GitHub/DLMDWPMP01---Programmieren-mit-Python/train.csv")
training.set_index('x',inplace=True)
test = pd.read_csv("/Users/micha/Documents/GitHub/DLMDWPMP01---Programmieren-mit-Python/test.csv")

print(ideal)
print(training)
print(test)


#Berechnung zum finden der vier idealen Funktionen
#Erster Versuch für y1
#Wir berechnen für jede Spalte der idealen Funktionen den Least Square Wert und vergleichen ob er niedriger als der vorherige ist.
#Falls ja merken wir uns die Spalte.
#Am Ende haben wir dann die passende Spalte
# Least Square ist dabei die Methode der kleinsten Quadrate

TrainValue = "y2"
LeastSquareLow = 999

for column in ideal.columns:
    sumSquared = []

    for row in training.index:

        diff = (training[TrainValue][row] - ideal[column][row]) ** 2
        sumSquared.append(diff)

    LeastSquareNew = sum(sumSquared)

    if LeastSquareNew < LeastSquareLow:  # check if a value of ideal
        # is lower than the actual value
        LeastSquareLow = LeastSquareNew
        idealFunction = column

print("TrainValue", TrainValue, "IdealPassend", idealFunction)


#Codeschnipsel least Square scheint zu stimmen
#Aber ich bekomme keinen Plot...

#style.use('ggplot')
#plt.grid(True, color="k")
#training.plot(y='y2', title='Train',)
#ideal.plot(y='y11', title='Ideal')
#plt.show()

#Warum auch immer geht es jetzt...
#Plots sollten gut passen
#Test für y2 noch nicht erfolgreich. Liefert x als Ergebnis
#y3 = y2 könnte passen
#y4 = y33 passt.
#y1=y36

#y2 passend zu y11. x muss sowohl in ideal als auch im train Datensatz als index ausgenommen werden.
#Ausnahme von nur ideal führt zu Fehlermeldung
#plot sieht passend aus

style.use('ggplot')

#1
fig, axs = plt.subplots(2)
fig.suptitle('Selektion idealer Funktionen für den Training-Datensatz')
training.plot(y='y1',color = 'blue',ax=axs[0])
ideal.plot(y='y36',color = 'blue',ax=axs[1])
axs[0].set_title('Training', font='11')
axs[1].set_title('Ideal', font='11')

for ax in axs.flat:
    ax.set(xlabel='', ylabel='')
    ax.label_outer()

plt.show()

#2
fig, axs = plt.subplots(2)
fig.suptitle('Selektion idealer Funktionen für den Training-Datensatz')
training.plot(y='y2',color = 'orange', ax=axs[0])
ideal.plot(y='y11',color = 'orange', ax=axs[1])
axs[0].set_title('Training', font='11')
axs[1].set_title('Ideal', font='11')

for ax in axs.flat:
    ax.set(xlabel='', ylabel='')
    ax.label_outer()

plt.show()

#3
fig, axs = plt.subplots(2)
fig.suptitle('Selektion idealer Funktionen für den Training-Datensatz')
training.plot(y='y3',color = 'green', ax=axs[0])
ideal.plot(y='y2',color = 'green', ax=axs[1])
axs[0].set_title('Training', font='11')
axs[1].set_title('Ideal', font='11')

for ax in axs.flat:
    ax.set(xlabel='', ylabel='')
    ax.label_outer()

plt.show()

#4
fig, axs = plt.subplots(2)
fig.suptitle('Selektion idealer Funktionen für den Training-Datensatz')
training.plot(y='y4',color = 'red', ax=axs[0])
ideal.plot(y='y33',color = 'red', ax=axs[1])
axs[0].set_title('Training', font='11')
axs[1].set_title('Ideal', font='11')

for ax in axs.flat:
    ax.set(xlabel='', ylabel='')
    ax.label_outer()

plt.show()

