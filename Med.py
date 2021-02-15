from pymongo import MongoClient
from datetime import timedelta as td
from pymongo import MongoClient
from MedOps import MedOps as mo
from MedDatabase import MedDatabase 
from datetime import datetime as dt

class Med:
    
    def __init__(self):
        super().__init__()
    
    #There are four tipes os varables here:
    
    # basic info and other classe's intances
    
    name = ""
    client = MongoClient("localhost", 27017)
    db = client.get_database("MEDS")
    col = db.get_collection("medLogs")
    md = MedDatabase(client=client, db=db, col=col)
    
    ## Intake measuring variables
    #---------------------------------------
    dosePerDay = 0.0
    cpPerDay = 0.0
    cpPerBox = 0.0
    boxPerDay = cpPerBox / cpPerDay
    pricePerBox = 0.0
    pricePerDay = boxPerDay * pricePerBox    
        
    # Size measuring variables
    #----------------------------------------------
    cpIcome = 0.0
    boxIncome = cpIcome / cpPerBox
    
    ##Althoug it's possibile to use cp(pills), dose(mg) and boxes(box)
    ## I'm taking cp as default for intake and box for delta calculations
    
    ## Time measuring variables
    #day, month, timedelta and now
    #----------------------------------------------
        

    # methods for gattering log info into dictionaries
    # --------------------------------------------------------------------------------
        

    def lastStorage(self):
        #storage methd
        t2 = dt.now()
        t1 = lastLogDate
        s1 = lastStorage
        s2 = self.boxPerDay * (t2-t1)+s1

    def nextBuyDate(self):
        #storage methd
        
        timeOne =  self.boxIncome + lastStorage()/ self.boxPerDay
        delta = td(days=timeOne)
        buyDate = dt.now() + delta
        return buyDate


    def log_time(self):
        log_time = {"now" : dt.now(),
                        "year": dt.now().year,
                        "month": dt.now().month,
                        "day": dt.now().day,
                        "hour": dt.now().hour,
                        "minute": dt.now().minute,
                        "second": dt.now().second}
    
    def log_intake(self):    
        log_intake = {"dosePerDay": self.dosePerDay,
                    "cpPerDay": self.cpPerDay,
                    "boxPerDay" : self.boxPerDay,
                    "pricePerDay": boxPerDay * self.pricePerBox}                                                                 
        return log_intake
        
    def log_income(self):
        boxIncome = self.cpIncome 
        log_income  = {"cpIncome": self.cpIncome,
                       "boxIncome": self.boxIncome,
                       "nextBuyDate": self.nextBuyDate()}
        return log_income
        
    
    # database Methods
    # ----------------------------------------------------------
    def logInsert_Med(self):
        log_med = {"name": self.name,
                   "time": self.log_time(), 
                   "log_intake": self.log_intake(),
                    "log_income": self.log_income()}
        self.md.logInsert(log=log_med())

    def loadLogs_Med(self):
        self.md.loadLogs()
        

    #     methods for a future query
    # --------------------------------------------------------------------------------

#    def pastMedStorage(self, timeZero):
#        return mo.deltaMain(timeZero=timeZero, timeOne=timeOne,
#                           sizeZero=None, sizeOne=numBox, boxPerDay=boxPerDay())
#
#   def futureMedStorage(self, timeOne):
#      timeZero = dt.now()
#     return mo.deltaMain(timeZero=timeZero, timeOne=timeOne,
#                        sizeZero=numBox, sizeOne=None, boxPerDay=boxPerDay())

Med().loadLogs_Med