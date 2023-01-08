#Diese Lösung wurden von Michael Schwarzmüller für den Kurs DLMDWPMP01 erstellt:

#Import der benötigten Bibliotheken
import pandas as pd
import sqlalchemy as db
import matplotlib.pyplot as plt
from matplotlib import style
import os
import math


#Abfrage der verwendeten Versionen
print('Diese Lösung wurde mit folgenden Versionen erstellt:')
print('sqlalchemy: ', db.__version__)
print('pandas: ', pd.__version__)
#print('matplotlib: ', plt.__version__)

#Abruf Laufwerkspfad
pfad = os.path.dirname(__file__)
print ("Verwendeter Laufwerkspfad:", pfad)

#Einlesen und Anzeige der csv-Dateien
ideal = pd.read_csv(os.path.join(pfad, "ideal.csv"))
ideal.set_index('x', inplace=True)
training = pd.read_csv(os.path.join(pfad, "train.csv"))
training.set_index('x', inplace=True)
test = pd.read_csv(os.path.join(pfad, "test.csv"))
test.sort_values(["x"], inplace= True)

print(ideal)
print(training)
print(test)

#Diese Funktion dient zum Plotten der vier Trainingsfunktionen
def plot_train():

    style.use('ggplot')
    fig, axs = plt.subplots(4)
    fig.suptitle('Trainingsdaten')
    training.plot(y='y1', color='blue', ax=axs[0])
    training.plot(y='y2', color='orange', ax=axs[1])
    training.plot(y='y3', color='green', ax=axs[2])
    training.plot(y='y4', color='red', ax=axs[3])


    for ax in axs.flat:
        ax.set(xlabel='', ylabel='')
        ax.label_outer()

    plt.show()


#Einfügen der Klassenlogik
#Einfügen einer benutzerdefinierten Exception

class MyException(Exception):
    def __init__(self):
        my_message = 'Fehler. Der Wert befindet sich nicht in unseren Vorgaben.'
        self.my_message = my_message


#Diese Klasse bildet die Eltern-Klasse für die lest_square Methode und der Variable TrainValue
class Vererbung():

    def __init__(self, TrainValue):
        self.TrainValue = TrainValue
    def least_square(self):
        pass

#Diese Klasse führt die Berechnung für den ersten Teil der Aufgabenstellung durch
class LeastSquare(Vererbung):
    def least_square(self, TrainValue):
        global idealFunction
        self.TrainValue = TrainValue

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


#Plotten der vier Trainingsfunktionen zu den vier gefundenen idealen Funktionen
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

    plt.show()

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

    plt.show()

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

    plt.show()

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

    plt.show()

#Erschaffen der Engine
#Ablegen der Daten in der SQLite Datenbank
connection = db.create_engine("sqlite:///database.sqlite")
training.to_sql('training',connection, if_exists='replace', index=True)
test.to_sql('test',connection, if_exists='replace', index=True)
ideal.to_sql('ideal',connection, if_exists='replace', index=True)




#Diese Funktion löst den zweiten Teil der Aufgabenstellung
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





#Dies ist die Hauptfunktion die das Programm orchestriert
def main():

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

    except IndexError:
        print("Fehler: Index nicht vorhanden")

    else:
        Alle_Ideal = pd.DataFrame(data_list)
        print(Alle_Ideal)
        Tabelle3 = pd.DataFrame(test_best_fit()).iloc[:,[0,1,7,6]]
        Tabelle3.to_sql('test', connection, if_exists='replace', index=True)
        print(Tabelle3)

        plot()
        plot_train()


    finally:
        print("end")


if __name__ == '__main__':
    main()
