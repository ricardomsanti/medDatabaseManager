import pandas as pd
from win10toast import ToastNotifier
from Med import Med as med
from MedDatabase import MedDatabase as md
from datetime import timedelta as td
from datetime import datetime as dt


class MainMeds:
    def __init__(self):
        self.dash = "==============================================================================================================================="
        self.m = med(name=None, dosePerDay=None, cpPerDay=None, cpPerBox=None, cpIncome=None, database=None)
        self.nameList = self.m.database.loadNameList()
        self.t = ToastNotifier()

    def start(self):
        print(self.dash)
        print()
        print("MainMeds started")
        print()
        print(self.dash)
        OpList = ["New data", "Data view"]
        menuSeries = pd.Series(OpList, index={1, 2})
        print()
        print(menuSeries.to_string())
        print()
        select = int(input("Please choose an option from the menu \n"))
        return select


    def newData(self):
        print("Please type the following data about the new medication \n")
        varList = ["name",
                   "dosePerDay",
                   "cpPerDay",
                   "cpPerBox",
                   "cpIncome"]
        varDict = {}
        for x in varList:
            value = input("{}: \n".format(x))
            varDict.update({str(x): value})
        self.m.name = varDict.get("name")
        self.m.dosePerDay = float(varDict.get("dosePerDay"))
        self.m.cpPerDay = float(varDict.get("cpPerDay"))
        self.m.cpPerBox = float(varDict.get("cpPerBox"))
        self.m.cpIncome = float(varDict.get("cpIncome"))
        self.m.database.newLog(log=self.m.logMed())

    def dataView(self):
        fullLogs = self.m.database.loadLogsFull()
        fullDict = {}
        nameList = []
        for x in fullLogs:
            for z, y in x.items():
                fullDict[z] = y
                if z == "name" and y not in nameList:
                    nameList.append(y)
        df = pd.DataFrame(fullDict, index=range(len(nameList)), columns=["id","name","time","dosePerDay",
                                           "cpPerDay" ,"cpPerBox" ,"cpIncome",
                                           "intake" ,"boxIncome","lastStorage",
                                             "storageToday","nextBuyDate"])

        print(df)

    def menuSelection(self):
        select = self.start()
        while select != "":
            if select == 1:
                self.newData()
                break
            elif select == 2:
                self.dataView()
                break
        if select == "":
            print("See you next time!")
        else:
            self.menuSelection()

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
mm.mainUpdate()
mm.menuSelection()
