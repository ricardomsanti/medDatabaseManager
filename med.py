from medDatabase import MedDatabase as md
from pymongo import MongoClient
from medOps import MedOps as mo
from datetime import datetime as dt
from datetime import timedelta as td
from datetime import timezone as tm
tm.utc

###########################################################################################################


class Med():
    
 
    
    
    def __init__(self, name, dosePerDay, cpPerDay, cpBox, boxPrice, cpNum):
        self.name = name
        self.dosePerDay = dosePerDay 
        self.cpPerDay = cpPerDay 
        self.cpBox = cpBox
        self.boxPrice  = boxPrice
        self.cpNum = cpNum
    
    #methods for gattering log info
    #--------------------------------------------------------------------------------                          
    
    def numBox(self):
        numBox = self.cpNum/ self.cpBox
        return numBox
        
    def doseBox(self):
        doseBox = self.cpBox / self.cpPerDay
        return doseBox
    
    def priceOverTime(self, days = 1):
        
        dip = self.dosePerDay / self.cpPerDay / self.cpBox * self.boxPrice * days
        return int(dip)
    
    def boxPerDay(self):
        
        boxPerDay =  self.cpPerDay / self.cpBox
        
        return float(boxPerDay)
    
    def nextBuyDate(self):
        
        #------------timedelta calculate
        
        boxPerDay = self.boxPerDay()
        sizeZero = self.numBox()
        sizeOne = 0.0
        timeZero = 0.0
        timeOne = timeZero - (sizeOne -sizeZero)/boxPerDay
        delta = td(days=timeOne)
        buyDate = dt.now() + delta
        #----------- date calculate
        return buyDate
        
    
    
    #methods for a future query
    #--------------------------------------------------------------------------------                      
    def lastBuyDate(self):
        timeOne = dt.now()
        boxPerDay = self.dosePerDay / doseBox
        return mo.deltaMain(timeZero=None, timeOne=timeOne,
                            sizeZero=numBox, sizeOne=0, boxPerDay= boxPerDay())
                            
    
    def pastMedStorage(self, timeZero):
        
        timeOne = dt.now()
        return mo.deltaMain(timeZero=timeZero, timeOne=timeOne,
                            sizeZero=None, sizeOne=numBox,boxPerDay= boxPerDay())
        
        
    def futureMedStorage(self, timeOne):
        
        timeZero = dt.now()
        return mo.deltaMain(timeZero=timeZero, timeOne=timeOne,
                            sizeZero=numBox, sizeOne=None,boxPerDay= boxPerDay())
        
        
        
    #log method
    #----------------------------------------------------------
    def logMed(self):
        client = MongoClient("localhost", 27017)   
        meds = client.get_database("MEDS")
        medLog = meds.get_collection("medLog")

        log_time = {"year": dt.now().year,
                    "month": dt.now().month,
                    "day": dt.now().day,
                    "hour": dt.now().hour,
                    "minute": dt.now().minute,
                    "second": dt.now().second
                        }
        
            
       
        log_med = { "name" : self.name,
                "dosePerDay": self.dosePerDay,
                "cpPerDay": self.cpPerDay,
                "cpBox": self.cpBox,
                "boxPrice": self.boxPrice,
                "cpNum" : self.cpNum,
                "nextBuyDate": self.nextBuyDate(),
                "time": log_time
                    }    
        medLog.insert_one(log_med)
        
                
