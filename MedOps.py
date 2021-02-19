from MedDatabase import MedDatabase as md
from Med import Med as m
from datetime import datetime as dt
from datetime import timedelta as td

#Responsible for instatiating the Med Class as well as the MedDatabase and performing the necessary calculation so new logs can be mande

class Med:

    def __init__(self):
        self.name
        self.dosePerDay
        self.cpPerDay
        self.cpPerBox
        self.pricePerBox
        self.cpIncome

        self.database = md()
        self.med = m()


    def boxPerDay(self):
        return self.med.cpPerBox / self.med.cpPerDay

    def pricePerBox(self):
        return self.boxPerDay * self.pricePerBox

    def boxIncome(self):
        return self.med.cpIncome / self.med.cpPerBox

    def logMed(self, newMed = "n"):
        if newMed == "n":
            log_med = {"name": self.med.name,
                       "time": dt.now(),
                       "intake": self.boxPerDay,
                       "income": self.boxIncome,
                       "storageToday":
                           self.StorageToday(med=self.med.name, income=self.boxIncome()),
                       "nexBuyDate": self.nextBuyDate(med=self.med.name,
                                                      income=self.boxIncome())}
        else:
            log_med = {"name": self.med.name,
                       "time": dt.now(),
                       "intake": self.boxPerDay,
                       "income": self.med.boxIncome,
                       "storageToday": self.boxIncome,
                       "nexBuyDate": self.nextBuyDate(med=self.med.name,
                                                      income=self.boxIncome())}



        return log_med

        # calculation methods
        # ----------------------------------------------------------------------

#how to do calculation with date objects

    def StorageToday(self, med, income=None):
        # based on the data from the last log, calculates the actual storage
        lasLog = self.database.loadLastLogs(med=med)
        t2 = dt.now()
        t1 = lasLog["time"]
        delta = t2 - t1
        s2 = int(self.med.boxPerDay()) * int(delta.microseconds)
        return s2 + income

    def nextBuyDate(self, med=None, income=None):
        # based on the data from the actual log, calculates the date of the next income
        t1 = self.boxIncome + self.StorageToday(med=med, income=income) / self.boxPerDay
        delta = td(days=t1)
        buyDate = dt.now() + delta
        return buyDate



