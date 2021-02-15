import unittest
from Med import Med


class TestMed(unittest.TestCase):
    m = Med(name="testMed", dosePerDay=2, cpPerDay=1, cpPerBox=30, pricePerBox=35.53, cpPerBuy=180)
    
    def test_numBox(self):
        """
        Tests if the function boxNum can retunr the proper number of boxes
        """
        result = self.m.boxNum()
        self.assertEqual(result, 6)
        
        
    def test_doseBox(self):
        """
        Tests if the function doseBox can return the proper dose per box
        """
        result = self.m.doseBox()
        self.assertEqual(result, 30)
        
    def text_priceOverTime(self):
        """
        Tests if this function can return the proper price per day
        """
        result = self.m.priceOverTime(days=1)
        self.assertEquals(result, 2.36)
    
    def test_numBox(self):
        """
        Tests if this function can return the proper number fo boxe
        """
        result = self.m.numBox()
        self.assertEquals(result, 6)
        
    def test_intake(self):
        """
        Tests if this funtion can return the proper amount in mg, cp and boxes
        """
        
        result1 = self.m.intake(unit="mg")
        result2 = self.m.intake(unit="cp")
        result3 = self.m.intake(unit="box")
        self.assertEqual(result1,2)
        self.assertEqual(result2,1.0)
        self.assertEqual("{:.2f}".format(result3),str(0.03))
        
    def test_nextBuyDate(self):
        """
        Tests if this funtion can return the proper date when the medication storate will be equals zero
        """
        result = self.m.nextBuyDate()
        print("Result: {}".format(result))
        self.assertEqual(result, 180)
        
        
        
if __name__ == '__main__':
    unittest.main()