import pandas as pd
import sqlalchemy as db
import matplotlib as plt
import numpy as np
import os
import math

#Erster Test
print('Diese Lösung wurde mit folgenden Versionen erstellt:')
print('sqlalchemy: ', db.__version__)
print('pandas: ', pd.__version__)
print('matplotlib: ', plt.__version__)

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

