import pandas as pd
import sqlalchemy as db
import matplotlib.pyplot as plt
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
training = pd.read_csv("/Users/micha/Documents/GitHub/DLMDWPMP01---Programmieren-mit-Python/train.csv")
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

TrainValue = "y1"
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

