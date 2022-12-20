import pandas as pd
import sqlalchemy as db
import matplotlib.pyplot as plt
from matplotlib import style
import os

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

#Einfügen der Klassenlogik

class Vererbung():
#Vererbungshierarchie einführen und ausführen
    def __init__(self, TrainValue):
        self.TrainValue = TrainValue

        pass



class LeastSquare(Vererbung):
    def least_square(self, TrainValue):
        self.TrainValue = TrainValue

            # Berechnung zum finden der vier idealen Funktionen
            # Erster Versuch für y1
            # Wir berechnen für jede Spalte der idealen Funktionen den Least Square Wert und vergleichen ob er niedriger als der vorherige ist.
            # Falls ja merken wir uns die Spalte.
            # Am Ende haben wir dann die passende Spalte
            # Least Square ist dabei die Methode der kleinsten Quadrate

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


        return idealFunction


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
axs[0].set_title('Training')
axs[1].set_title('Ideal')

for ax in axs.flat:
    ax.set(xlabel='', ylabel='')
    ax.label_outer()

#plt.show()

#2
fig, axs = plt.subplots(2)
fig.suptitle('Selektion idealer Funktionen für den Training-Datensatz')
training.plot(y='y2',color = 'orange', ax=axs[0])
ideal.plot(y='y11',color = 'orange', ax=axs[1])
axs[0].set_title('Training')
axs[1].set_title('Ideal')

for ax in axs.flat:
    ax.set(xlabel='', ylabel='')
    ax.label_outer()

#plt.show()

#3
fig, axs = plt.subplots(2)
fig.suptitle('Selektion idealer Funktionen für den Training-Datensatz')
training.plot(y='y3',color = 'green', ax=axs[0])
ideal.plot(y='y2',color = 'green', ax=axs[1])
axs[0].set_title('Training')
axs[1].set_title('Ideal')

for ax in axs.flat:
    ax.set(xlabel='', ylabel='')
    ax.label_outer()

#plt.show()

#4
fig, axs = plt.subplots(2)
fig.suptitle('Selektion idealer Funktionen für den Training-Datensatz')
training.plot(y='y4',color = 'red', ax=axs[0])
ideal.plot(y='y33',color = 'red', ax=axs[1])
axs[0].set_title('Training')
axs[1].set_title('Ideal')

for ax in axs.flat:
    ax.set(xlabel='', ylabel='')
    ax.label_outer()

#plt.show()


#Teil 2 Funktionstest:
#Welche der 4 idealen Funktionen passt an besten zu den Test Punkten
#Aber am Ende kleiner sqrt 2

#Ersetze Training durch Ideal

#Bestimme für jede Spalte den nächsten Fit solange kleiner als sqrt2

#Schreibe Lösung in Tabelle


#Daten in SQL Datenbank legen
connection = db.create_engine("sqlite:///database.sqlite")
training.to_sql('training',connection, if_exists='replace', index=True)
test.to_sql('test',connection, if_exists='replace', index=True)
ideal.to_sql('ideal',connection, if_exists='replace', index=True)

#index True anstelle von 'x'
