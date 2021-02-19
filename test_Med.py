import unittest
from Med import Med
from MedDatabase import MedDatabase as md
from datetime import datetime as dt
class TestMed(unittest.TestCase):
    m = Med(name = "testMed", cpPerDay = 2, cpPerBox=20, cpIncome=40, dosePerDay=5, 
             database= md())
    
    def test_boxPerDay(self):
                """
                Returns cpPerBox x cpPerDay
                """
                result = self.m.boxPerDay()
                self.assertEqual(result, 0.1)
    def test_boxIncome(self):
                """
                Returns boxPerDay x pricePerBox
                """
                result = self.m.boxIncome()
                self.assertEqual(result,2)
        
    def test_logMedNew(self):
                """
                Returns a dict made from a new med info
                """
                newLoG = {"name": self.m.name,
                            "time": dt.now(),
                            "intake": 0.1,
                            "income": 2,
                            "storageToday": 2,
                            "nexBuyDate": 20}
                result = self.m.logMed(newMed="y")
                self.assertCountEqual(result, newLoG)
        
    def test_logMed(self):
                """
                Returns a dict made using previous information from a already present in the
                database med
                """
                
        
        
        
if __name__ == '__main__':
    unittest.main()