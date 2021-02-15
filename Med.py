from datetime import datetime as dt
import bson
from bson.codec_options import CodecOptions as co
import pandas as pd
from pymongo import MongoClient
from MedDatabase import MedDatabase




class Med:

    def __init__(self, client, db, col):
        self.client = client
        self.db = db
        self.col = col

    
    #There are four tipes os varables here:
    
    # basic info and other classe's intances
    
    name = ""

    
    ## Intake measuring variables
    #---------------------------------------
    dosePerDay =None
    cpPerDay = None
    cpPerBox =None
    boxPerDay = cpPerBox / cpPerDay
    pricePerBox =None
    pricePerDay = boxPerDay * pricePerBox    
        
    # Size measuring variables
    #----------------------------------------------
    cpIcome =None
    boxIncome = cpIcome / cpPerBox
    
    ##Althoug it's possibile to use cp(pills), dose(mg) and boxes(box)
    ## I'm taking cp as default for intake and box for delta calculations
    
    ## Time measuring variables
    #day, month, timedelta and now
    #----------------------------------------------
        

    # methods for gattering log info into dictionaries
    # --------------------------------------------------------------------------------
        



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
                    "pricePerDay": self.boxPerDay * self.pricePerBox}
        return log_intake
        
    def log_income(self):
        boxIncome = self.cpIncome 
        log_income  = {"cpIncome": self.cpIncome,
                       "boxIncome": self.boxIncome,
                       "nextBuyDate": self.nextBuyDate()}
        return log_income
        
    
    # database Methods
    #----------------------------------------------------------------------
    def newLog(self):
        log_med = {"name": self.name,
                   "time": self.log_time(), 
                   "log_intake": self.log_intake(),
                    "log_income": self.log_income()}
        self.col.insert_one(log_med)

    def loadLogsFull(self):
        loadLogs = []
        posts = self.col.find()
        for post in posts:
            loadLogs.append(dict(post))
        return loadLogs

    def loadNameList(self):
        # queries the database returning only medication names
        logs = self.loadLogsFull()
        nameList = [post["name"] for post in logs]
        return nameList

    def loadLogsMed(self, med):
        #queries the database returning only the logs which math a certain name
        logs = self.loadLogsFull()
        logsMed = [post for post in logs if post["name"] == med]
        return logsMed

    def loadLastLogs(self, med):
        # queries the database returning only the last logged log
        logs = self.loadLogsMed(med=med)
        selectLogList = [post for post in logs[(len(logs) - int(1)): len(logs)]]
        return selectLogList



    #calculation methods
    #----------------------------------------------------------------------
    def StorageToday(self, med, income=None):
        # based on the data from the last log, calculates the actual storage
        lasLog = self.loadLastLogs(med=med)
        log_time = lasLog["log_time"]
        t2 = dt.now()
        t1 = log_time["now"]
        s2 = self.boxPerDay * (t2 - t1)
        return s2 + income

    def nextBuyDate(self, med=None, income=None):
        # based on the data from the actual log, calculates the date of the next income
        t1 = self.boxIncome + self.StorageToday(med=med, income=income) / self.boxPerDay
        delta = td(days=t1)
        buyDate = dt.now() + delta
        return buyDate

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
client = MongoClient("localhost", 27017)
db = client.get_database("MEDS")
col = db.get_collection("medLog")
md = Med(client=client, db=db, col=col)
print(md.loadLogsFull())
print()
print()
print(md.loadLastLogs(num = 2))
print()
print()
print(md.loadLogsMed())
