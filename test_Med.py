import unittest
from Med import Med
from MedDatabase import MedDatabase as md
from datetime import datetime as dt
class TestMed(unittest.TestCase):
    m = Med(name = "testMed", cpPerDay = 2, cpPerBox=20, cpIncome=40, dosePerDay=5,
             database= md(), intake=None, income=None)
    
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
                log = {"name": self.m.name,
                          "time": dt.now(),
                          "intake": 0.1,
                          "income": 2,
                          "storageToday": 2,
                          "nexBuyDate": 20}
                result = self.m.logMed(newMed="y")
                self.assertCountEqual(result, log)
                
        

    def test_storageToday(self):
                m2 = Med(name="med3", intake=2, dosePerDay=15, cpPerDay=1, cpPerBox=30, cpIncome=60,
                         database=md(), income=0)
                """
                Returns the current storage
                """
                result = m2.storageToday(med="med3")
                self.assertEqual(result, 1.7)



    def test_nextBuyDate(self):
                m2 = Med(name="med3", intake=2, dosePerDay=15, cpPerDay=1, cpPerBox=30, cpIncome=60,
                 database=md(), income=0)
                """
                Returns the time whem a a given medication will end
                """
                result = m2.nextBuyDate(med="med3")
                self.assertEqual(result,dt(2021, 4, 14, 20, 41, 17, 622320))

if __name__ == '__main__':
    unittest.main()