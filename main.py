import pandas as pd
import sqlalchemy as db
import matplotlib.pyplot as plt
from matplotlib import style
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
ideal = pd.read_csv(os.path.join(pfad, "ideal.csv"))
ideal.set_index('x', inplace=True)
training = pd.read_csv(os.path.join(pfad, "train.csv"))
training.set_index('x', inplace=True)
test = pd.read_csv(os.path.join(pfad, "test.csv"))
test.sort_values(["x"], inplace= True)

print(ideal)
print(training)
print(test)

#Einfügen der Klassenlogik
#Einfügen von Exceptions

class MyException(Exception):
    def __init__(self):
        my_message = 'Fehler. Der Wert befindet sich nicht in unseren Vorgaben.'
        self.my_message = my_message

class Vererbung():
#Vererbungshierarchie einführen und ausführen
    def __init__(self, TrainValue):
        self.TrainValue = TrainValue
    def calculate_least_square(self):
        pass


class LeastSquare(Vererbung):
    def least_square(self, TrainValue):
        global idealFunction
        self.TrainValue = TrainValue

        # Berechnung zum finden der vier idealen Funktionen
        # Erster Versuch für y1
        # Wir berechnen für jede Spalte der idealen Funktionen den Least Square Wert und vergleichen ob er niedriger als der vorherige ist.
        # Falls ja merken wir uns die Spalte.
        # Am Ende haben wir dann die passende Spalte
        # Least Square ist dabei die Methode der kleinsten Quadrate
        # Versuch mit AlleIdeal die vier Spalten der Idealen Funktionen zu speichern.
        # Zusätzliche Funktion Haupt angelegt

        if TrainValue not in ['y1', 'y2', 'y3', 'y4']:
            raise MyException

        else:
            LeastSquareLow = 999
            for column in ideal.columns:
                sumSquared = []

                for row in training.index:

                    diff = (training[TrainValue][row] - ideal[column][row]) ** 2
                    sumSquared.append(diff)

                LeastSquareNew = sum(sumSquared)

                if LeastSquareNew < LeastSquareLow:

                    LeastSquareLow = LeastSquareNew
                    idealFunction = column

            #print("Train", TrainValue, "=Ideal", idealFunction)
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



def plot():

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

#Daten in SQL Datenbank legen
connection = db.create_engine("sqlite:///database.sqlite")
training.to_sql('training',connection, if_exists='replace', index=True)
test.to_sql('test',connection, if_exists='replace', index=True)
ideal.to_sql('ideal',connection, if_exists='replace', index=True)



#index True anstelle von 'x'

#Speichern der Werte funktioniert nicht....
#Warum weiß ich noch nicht
#Funktioniert mit der Main Funktion
#Ausgabe der Tabelle mit den idealen Funktionen läuft jetzt auch

#Teil 2 Funktionstest:
#Welche der 4 idealen Funktionen passt an besten zu den Test Punkten
#Aber am Ende kleiner sqrt 2

def test_best_fit():
    test_neu = test.join(Alle_Ideal, on='x')

    for column in test_neu.columns[2:6]:
        for row in test_neu.index:
            cal = abs(test_neu['y'][row] - test_neu[column][row])


            if 0 < cal <= math.sqrt(2):
                test_neu.loc[row, 'Id Fkt.'] = column
                test_neu.loc[row, 'Delta Y'] = cal

    test_neu.to_sql('test', connection, if_exists='replace', index=True)

    NaN = {}
    for row in test_neu.index:
        if pd.isnull(test_neu['Id Fkt.'][row]):
            NaN[test_neu['x'][row]] = [test_neu['y'][row]]

    NaN_df = pd.DataFrame.from_dict(data=NaN, orient='index', columns=['y'])
    NaN_df.reset_index(inplace=True)
    print(NaN_df)

    style.use('ggplot')
    #test_neu.plot(x='x', y='y', kind='scatter', label='Testdatensatz', title= 'Visualisierung Test zu Ideal')
    #test_neu.plot(x='x', y='y11', kind='line', label='y11', color='red', title= 'Visualisierung Test zu Ideal')

    plt.scatter(test_neu['x'], test_neu['y36'], linewidth=0.1, color='blue', label='Ideal y36')
    plt.scatter(test_neu['x'], test_neu['y11'], linewidth=0.1, color='orange', label='Ideal y11')
    plt.scatter(test_neu['x'], test_neu['y2'], linewidth=0.1, color='green', label='Ideal y2')
    plt.scatter(test_neu['x'], test_neu['y33'], linewidth=0.1, color='red', label='Ideal y33')
    plt.scatter(test_neu['x'], test_neu['y'], label='Testdatensatz', color='grey')
    plt.scatter(NaN_df['index'], NaN_df['y'] , label='NaN sqrt2', color='black')
    plt.title('Vergleich Testdatensatz zu Idealdaten', fontsize=16)
    plt.legend(fontsize=8, loc='upper center', facecolor='white')
    #plt.show()


    return test_neu

#Bestimme für jede Spalte den nächsten Fit solange kleiner als sqrt2

#Schreibe Lösung in Tabelle





def main():
#Erzeugen der globalen Variable für den DataFrame
    global Alle_Ideal
    global Tabelle3


    Y1 = LeastSquare('y1')
    Y2 = LeastSquare('y2')
    Y3 = LeastSquare('y3')
    Y4 = LeastSquare('y4')

    try:
        data_list = {Y1.least_square(Y1.TrainValue): ideal[Y1.least_square(Y1.TrainValue)],
                    Y2.least_square(Y2.TrainValue): ideal[Y2.least_square(Y2.TrainValue)],
                    Y3.least_square(Y3.TrainValue): ideal[Y3.least_square(Y3.TrainValue)],
                    Y4.least_square(Y4.TrainValue): ideal[Y4.least_square(Y4.TrainValue)]}

    except SyntaxError:
        print("FehlerSyntax")

    else:
        Alle_Ideal = pd.DataFrame(data_list)
        print(Alle_Ideal)
        Tabelle3 = pd.DataFrame(test_best_fit()).iloc[:,[0,1,7,6]]
        Tabelle3.to_sql('test', connection, if_exists='replace', index=True)
        print(Tabelle3)

        plot()


    finally:
        print("end")

""" This part of the script will only by executed
 if the script is called directly
 """
if __name__ == '__main__':
    main()