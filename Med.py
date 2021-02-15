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
    dosePerDay =1.0
    cpPerDay = 1
    cpPerBox =1.0
    boxPerDay = cpPerBox / cpPerDay
    pricePerBox =1.0
    pricePerDay = boxPerDay * pricePerBox    
        
    # Size measuring variables
    #----------------------------------------------
    cpIcome =1.0
    boxIncome = cpIcome / cpPerBox
    
    ##Althoug it's possibile to use cp(pills), dose(mg) and boxes(box)
    ## I'm taking cp as default for intake and box for delta calculations
    
    ## Time measuring variables
    #day, month, timedelta and now
    #----------------------------------------------
        

    # methods for gattering log info into dictionaries
    # --------------------------------------------------------------------------------
        

    """def lastStorage(self):
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
"""

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
        self.col.insert_one(log_med)


    def loadLogs(self, selectMed=None, selectLastLogs=None):
        selectLogList = []
        singleLog = {}
        loadLogs = []
        posts = self.col.find()
        nameList = []
        #return loadLogs
        if selectMed is None:
            if selectLastLogs is None:
                for post in posts:
                    singleLog = dict(post)
                    loadLogs.append(singleLog)        
                    selectLogList = loadLogs
            elif selectLastLogs is not None:
                for post in posts:
                    singleLog = dict(post)
                    loadLogs.append(singleLog)
                selectLogList = [x for x in loadLogs[(len(loadLogs) - int(selectLastLogs)): len(loadLogs)]]
        elif selectMed == "y":
            if selectLastLogs is None:
                for post in posts:
                    singleLog = dict(post)
                    loadLogs.append(singleLog)        
                    nameList.append(singleLog["name"])
                nameSeries = pd.Series(nameList, index=["med1", "med2", "med3", "med4", "med5", "med6"])
                print(nameSeries)
                name = input("Please choose a medication from the list \n")
                
                #-----------------------------------------------------having trouble performing this selection
                #all the other ones are working properly, may be i should split the function in two
                new_posts = self.col.find({"name":str(name)})
                for post in new_posts:
                    singleLog = dict(post)
                    loadLogs.append(singleLog)
                selectLogList = loadLogs
            elif selectLastLogs is not None:
                for post in posts:
                    singleLog = dict(post)
                    loadLogs.append(singleLog)
                selectLogList = [x for x in loadLogs[(len(loadLogs) - selectLastLogs): len(loadLogs)]]

        return selectLogList


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
