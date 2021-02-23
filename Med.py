from MedDatabase import MedDatabase as md
from datetime import datetime as dt
from datetime import timedelta as td

#Responsible for instatiating the Med Class as well as the MedDatabase and performing the necessary calculation so new logs can be mande

class Med:

    def __init__(self, name, dosePerDay, 
                 cpPerDay, cpPerBox, 
                 cpIncome, database):
        self.name = name
        self.dosePerDay = dosePerDay
        self.cpPerDay = cpPerDay
        self.cpPerBox = cpPerBox
        self.cpIncome = cpIncome
        self.database = md()





    def boxPerDay(self):
        boxPerDay = float(self.cpPerDay/self.cpPerBox)
        return boxPerDay

    def boxIncome(self):
        result = float(self.cpIncome / self.cpPerBox)
        return result

    def logMed(self):
        log_med = {"name": self.name,
                   "time": dt.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                   "dosePerDay": self.dosePerDay,
                   "cpPerDay": self.cpPerDay,
                   "cpPerBox": self.cpPerBox,
                   "cpIncome":self.cpIncome,
                   "intake": self.boxPerDay(),
                   "boxIncome": self.boxIncome(),
                   "lastStorage" : self.lastStorage(),
                   "storageToday": self.storageToday(),
                   "nextBuyDate": self.nextBuyDate()}
        return log_med

        # calculation methods
        # ----------------------------------------------------------------------

#how to do calculation with date objects
    def lastStorage(self):
        lastLog = self.database.loadLastLogs(med=self.name)
        lastStorage = lastLog.get("lastStorage")
        return lastStorage

    def storageToday(self):
        # based on the data from the last log, calculates the actual storage
        storage = 0
        lastLog = self.database.loadLastLogs(med=self.name)
        srtTime = lastLog.get("time")
        t1 = dt.strptime(str(srtTime),"%Y-%m-%dT%H:%M:%S.%fZ")
        t2 = dt.now()
        delta = t2 - t1
        s2 = (self.boxPerDay() * int(delta.days)) + self.boxIncome()
        storage = self.lastStorage() - s2
        return storage

    def nextBuyDate(self):
        # based on the data from the actual log, calculates the date of the next income
        t1 = self.storageToday() / self.boxPerDay()
        delta = td(days=t1)
        buyDate = dt.now() + delta
        return buyDate



