from task1Code import *
import unittest

class SquareUnitTest(unittest.TestCase):
    def test1(self):
        assert square(2) == 4, "can't find square of the the number"

    def test2(self):
        assert square(-3) ==  9, "can't find square of the negative number"

    def test3(self):
        assert square(0) ==  0, "can't find square of the number 0"

class ProductUnitTest(unittest.TestCase):
    def test1(self):
        assert product(1, 2) == 2, "can't multiply positive numbers"

    def test2(self):
        assert product(-1, -2) == 2, "can't multiply negative numbers"

    def test3(self):
        assert product(-10, 10) == -100, "can't multiply negative and positive numbers"

class QuotientUnitTest(unittest.TestCase):
    def test1(self):
        assert quotient(4, 2) == 2, "can't divide positive numbers"

    def test2(self):
        assert quotient(-8, -2) == 4, "can't divide negative numbers"

    def test3(self):
        assert quotient(-8, 2) == -4, "can't divide by zero"

class SumUnitTest(unittest.TestCase):
    def test1(self):
        assert summ(5, 7) == 12, "can't find sum of positive numbers"

    def test2(self):
        assert summ(-3, -9) == -12, "can't find sum of negative numbers"

    def test3(self):
        assert summ(-10, 33) == 23, "can't find sum of negative and positive numbers"


class DifferenceUnitTest(unittest.TestCase):
    def test1(self):
        assert difference(6, 8) == -2, "can't find difference of positive numbers"

    def test2(self):
        assert difference(-5, -2) == -3, "can't find difference of negative numbers"

    def test3(self):
        assert difference(-5, 9) == -14, "can't find difference of negative and positive numbers"


def squareSuite():
    suite = unittest.TestSuite()
    suite.addTest(SquareUnitTest('test1'))
    suite.addTest(SquareUnitTest('test2'))
    suite.addTest(SquareUnitTest('test3'))
    return suite


def productSuite():
    suite = unittest.TestSuite()
    suite.addTest(ProductUnitTest('test1'))
    suite.addTest(ProductUnitTest('test2'))
    suite.addTest(ProductUnitTest('test3'))
    return suite



def quotientSuite():
    suite = unittest.TestSuite()
    suite.addTest(QuotientUnitTest('test1'))
    suite.addTest(QuotientUnitTest('test2'))
    suite.addTest(QuotientUnitTest('test3'))
    return suite

def sumSuite():
    suite = unittest.TestSuite()
    suite.addTest(SumUnitTest('test1'))
    suite.addTest(SumUnitTest('test2'))
    suite.addTest(SumUnitTest('test3'))
    return suite

def differenceSuite():
    suite = unittest.TestSuite()
    suite.addTest(DifferenceUnitTest('test1'))
    suite.addTest(DifferenceUnitTest('test2'))
    suite.addTest(DifferenceUnitTest('test3'))
    return suite

def main():
    print("--- Name: Muhammad Sulaiman Sultan\n--- Roll No: 231453415\n--- Instructor: Dr. Saad Bin Saleem\n--- Welcome to the test suite for Assignment1")
    while 1:
        option = input("\nPlease select a unit test or suite: \n1. Square\n2. Product\n3. Quotient\n4. Sum\n5. Difference\n6. Entire Test Suite\n7. Exit\n")
        if option == '1':
            suite = squareSuite()
            unittest.TextTestRunner(verbosity = 2).run(suite)
        elif option == '2':
            suite = productSuite()
            unittest.TextTestRunner(verbosity = 2).run(suite)
        elif option == '3':
            suite = quotientSuite()
            unittest.TextTestRunner(verbosity = 2).run(suite)
        elif option == '4':
            suite = sumSuite()
            unittest.TextTestRunner(verbosity = 2).run(suite)
        elif option == '5':
            suite = differenceSuite()
            unittest.TextTestRunner(verbosity = 2).run(suite)
        elif option == '6':
            suite = unittest.TestSuite([squareSuite(), productSuite(), quotientSuite(), sumSuite(), differenceSuite()])
            unittest.TextTestRunner(verbosity = 2).run(suite)
        elif option == '7':
            break
        else:
            print("---Invalid selection---")

if __name__ == '__main__':
    main()