from datetime import datetime as dt
from typing import Any

#Responsible for gathering data from user's input or database operations, allthough none of the
#proper calculation happens here

class Med:

    def __init__(self, name=None, dosePerDay=None,
                 cpPerDay=None, cpPerBox=None, pricePerBox=None, cpIncome=None):
        self.name = name
        self.dosePerDay = dosePerDay
        self.cpPerDay = cpPerDay
        self.cpPerBox = cpPerBox
        self.pricePerBox = pricePerBox
        self.cpIncome = cpIncome


    def boxPerDay(self):
        return self.cpPerBox / self.cpPerDay

    def pricePerBox(self):
        return self.boxPerDay * self.pricePerBox

    def boxIncome(self):
        return self.cpIncome / self.cpPerBox

    def logMed(self):
        log_med = {"name": self.name,
                   "time": dt.now(),
                   "intake": self.boxPerDay,
                   "income": self.boxIncome,
                   "storageToday":
                       self.StorageToday(med=self.name,income=self.boxIncome()),
                   "nexBuyDate": self.nextBuyDate(med=self.name,
                                                  income=self.boxIncome())}
        return log_med

    # calculation methods
    # ----------------------------------------------------------------------
    def StorageToday(self, med, income=None):
        # based on the data from the last log, calculates the actual storage
        lasLog = self.loadLastLogs(med=med)
        t2 = dt.now()
        t1 = lasLog["time"]
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
