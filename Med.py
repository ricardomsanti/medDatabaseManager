from MedDatabase import MedDatabase as md
from datetime import datetime as dt
from datetime import timedelta as td

#Responsible for instatiating the Med Class as well as the MedDatabase and performing the necessary calculation so new logs can be mande

class Med:

    def __init__(self, name, dosePerDay, 
                 cpPerDay, cpPerBox, 
                 cpIncome, database, intake, income):
        self.name = name
        self.dosePerDay = dosePerDay
        self.cpPerDay = cpPerDay
        self.cpPerBox = cpPerBox
        self.cpIncome = cpIncome
        self.database = md()
        self.intake = intake
        self.income = income



    def boxPerDay(self):
        cpPerDay = self.cpPerDay
        cpPerBox = self.cpPerBox
        if self.cpPerDay or self.cpPerBox is None:
            lastLog = self.database.loadLastLogs()
            boxPerDay = lastLog.get("intake")
        else:
            boxPerDay = float(cpPerDay/cpPerBox)
        return boxPerDay

    def boxIncome(self):
        cpIncome = self.cpIncome
        cpPerBox = self.cpPerBox
        if self.cpIncome in None or self.cpPerBox is None:
            lastLog = self.database.loadLastLogs(med=self.name)
            boxIncome = lastLog.get("income")
        else:
            result = float(self.cpIncome / self.cpPerBox)
        return boxIncome

    def logMed(self, newMed="n"):
        if newMed != "n":
            log_med = {"name": self.name,
                       "time": dt.now(),
                       "intake": self.boxPerDay(),
                       "income": self.boxIncome(),
                       "lastStorage" : self.lastStorage(),
                       "storageToday": self.boxIncome(),
                       "nextBuyDate": self.boxIncome()/self.boxIncome()}
        else:
            log_med = {"name": self.name,
                       "time": dt.now(),
                       "intake": self.intake,
                       "income": self.income,
                       "lastStorage" : self.lastStorage(),
                       "storageToday": self.storageToday(),
                       "nextBuyDate": self.nextBuyDate(med=self.name,
                                                      income=self.boxIncome())}



        return log_med

        # calculation methods
        # ----------------------------------------------------------------------

#how to do calculation with date objects
    def lastStorage(self):
        lastLog = self.database.loadLastLogs(med=self.name)
        if lastLog is not None:
            lastStorage = 0
        else:
            lastStorage = lastLog.get("lastStorage")

        return lastStorage

    def storageToday(self):
        # based on the data from the last log, calculates the actual storage
        storage = 0
        lastLog = self.database.loadLastLogs(med=self.name)
        t1 = lastLog.get("time")
        t2 = dt.now()
        delta = t2 - t1
        s2 = (self.boxPerDay() * int(delta.days)) + self.income
        storage = self.lastStorage() - s2
        return storage

    def nextBuyDate(self):
        # based on the data from the actual log, calculates the date of the next income
        t1 = self.storageToday() / self.boxPerDay()
        delta = td(days=t1)
        buyDate = dt.now() + delta
        return buyDate



