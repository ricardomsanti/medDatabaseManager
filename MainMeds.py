
import pandas as pd
from win10toast import ToastNotifier
from Med import Med as med
from MedDatabase import MedDatabase as md
from datetime import timedelta as td
from datetime import datetime as dt


class MainMeds:
    def __init__(self):
        self.dash = "==============================================================================================================================="
        self.m = med(name=None, dosePerDay=None, cpPerDay=None, cpPerBox=None, cpIncome=None)
        self.nameList = self.m.database.loadNameList()
        self.t = ToastNotifier()
        self.select = 0

    def start(self):
        t = 0
        print(self.dash)
        print()
        print("MainMeds started")
        print()
        print(self.dash)
        OpList = ["New data", "Data view", "Main Update", "Price View", "Exit application"]
        menuSeries = pd.Series(OpList, index={1, 2, 3, 4, 5})
        print()
        print(menuSeries.to_string())
        print()
        self.select = int(input("Please choose an option from the menu \n"))
        return self.select


    def newData(self):
        print("Please type the following data about the new medication \n")
        varList = ["name",
                   "dosePerDay",
                   "cpPerDay",
                   "cpPerBox",
                   "cpIncome",
                   "pricePerBox"]
        varDict = {}
        for x in varList:
            value = input("{}: \n".format(x))
            varDict.update({str(x): value})
        self.m.name = varDict.get("name")
        self.m.dosePerDay = float(varDict.get("dosePerDay"))
        self.m.cpPerDay = float(varDict.get("cpPerDay"))
        self.m.cpPerBox = float(varDict.get("cpPerBox"))
        self.m.cpIncome = float(varDict.get("cpIncome"))
        self.m.pricePerBox = float(varDict.get("pricePerBox"))
        self.m.database.newLog(log=self.m.logNewMed())

    def dataView(self):
        df = pd.DataFrame(self.m.database.loadLogsFull(),
                          columns=["id", "name","time","dosePerDay",
                                                      "cpPerDay", "cpPerBox", "cpIncome",
                                                  "intake", "boxIncome", "lastStorage",
                                                  "storageToday", "nextBuyDate", "pricePerBox"])
        print(df)

    #attentio nedded hereby3
    def priceCalculator(self):
        self.m.priceOverTime()


    def menuSelection(self):
        self.select = self.start()
        if self.select == 1:
            self.newData()
        elif self.select == 2:
            self.dataView()
        elif self.select == 3:
            self.mainUpdate()
        elif self.select == 4:
            self.priceCalculator()
        return self.select


    def mainUpdate(self):
        # lista de nomes
        nameList = self.m.database.loadNameList()
        dateControl = {}
        for name in nameList:
            lastLog = self.m.database.loadLastLogs(med=name)
            self.m.name = lastLog.get("name")
            self.m.dosePerDay = lastLog.get("dosePerDay")
            self.m.cpPerDay = lastLog.get("cpPerDay")
            self.m.cpPerBox = lastLog.get("cpPerBox")
            self.m.cpIncome = lastLog.get("cpIncome")
            self.m.pricePerBox = lastLog.get("pricePerBox")
            buyDate = self.m.nextBuyDate()
            self.m.database.newLog(log=self.m.logMed())
            dateControl.update({self.m.name: buyDate})

        for x, y in dateControl.items():
            nextBuyDate = y
            today = dt.now()
            delta = nextBuyDate - today

            if delta.days < 8:
                self.t.show_toast(title="--Medication shopping alert---",
                                  msg="{} storage end in less than a week".format(x),
                                  threaded=True,
                                  duration=5)
            else:
                continue


###########################################################################################################


mm = MainMeds()

menu = mm.menuSelection()
while menu <= 4:
    menu = mm.menuSelection()
print("See you next time")



