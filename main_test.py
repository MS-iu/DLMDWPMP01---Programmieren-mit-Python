import unittest
import main
from main import MyException

class MyTestCase(unittest.TestCase):

    def test_least_square(self):

        #Prüfen auf Funktion der vier Traiingsdatensätze

        Y1 = main.LeastSquare('y1')
        Y2 = main.LeastSquare('y2')
        Y3 = main.LeastSquare('y3')
        Y4 = main.LeastSquare('y4')

        self.assertEqual(Y1.least_square(Y1.TrainValue), 'y36', 'Fehler: y36 erwartet')
        self.assertEqual(Y1.least_square(Y2.TrainValue), 'y11', 'Fehler: y11 erwartet')
        self.assertEqual(Y1.least_square(Y3.TrainValue), 'y2', 'Fehler: y2 erwartet')
        self.assertEqual(Y1.least_square(Y4.TrainValue), 'y33', 'Fehler: y33 erwartet')



    def test_least_square_2(self):

        with self.assertRaises(MyException):
            main.LeastSquare('y5').least_square(main.LeastSquare('y5').TrainValue)

    def test_test_best_fit(self):

        #Prüfen auf leere Rückgabewerte

        main.main()
        self.assertIsNotNone(main.test_best_fit())





if __name__ == '__main__':
    unittest.main()
