import unittest #Importing the unittest library
from temperature import Temperature #From the temperature.py file, import the Temperature class

class temperatureTest(unittest.TestCase): #Class for testing temperature
    def testarg(self):
        Temperature(celsius=20, fahrenheit=50) #Testing for the output error one argument only

    def testNeg(self):
        Temperature(-1) #Testing for the output error to be negative

    def testTemp1(self):
        Temperature(kelvin=273.15) #Testing for the output to be true for temperature

    def testTemp2(self):
        Temperature(celsius=30) #Testing for the output to be true for temperature

if __name__ == "__main__":
    unittest.main()
