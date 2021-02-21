import pandas as pd
from instagram_explore import media
from win10toast import ToastNotifier
from Med import Med as med
from MedDatabase import MedDatabase as md
from datetime import timedelta as td
from datetime import datetime as dt


class MainMeds:
    def __init__(self):
        self.dash = "==============================================================================================================================="
        self.m = med(name=None, dosePerDay=None, cpPerDay=None, cpPerBox=None, cpIncome=None, database=None,
                     intake=None, income=None)
        self.nameList = self.m.database.loadNameList()
        self.lastLog = self.m.database.loadLastLogs(med=None)
        self.t = ToastNotifier()

    def start(self):
        print(self.dash)
        print()
        print("MainMeds started")
        print()
        print(self.dash)
        OpList = ["Data update", "New data", "Data view"]
        menuSeries = pd.Series(OpList, index={1, 2, 3})
        print()
        print(menuSeries.to_string())
        print()
        select = int(input("Please choose an option from the menu \n"))
        return select

    def update(self):
        nameList = self.nameList
        nameSeries = pd.Series(nameList)
        print(nameSeries.to_string())
        medName = input("Please choose a medication to update from the list \n")
        print(self.dash)
        print()
        self.lastLog(med=medName)
        print("Last log data retrieved successflly. \n Please type in a new value in case of update, \n"
              "or just hit enter for the next item \n")
        print(self.dash)
        print()
        newLog = {}
        for x, y in self.lastLog.items():
            value = input("Field: {}    Current value: {} \n".format(x, y))
            if y == "":
                newLog[str(x)] = {value}
            else:
                newLog[str(x)] = {y}
        for x, y in newLog.items():
            print(x, y)

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
            self.m.name = varDict["name"]
            self.m.dosePerDay = float(varDict["dosePerDay"])
            self.m.cpPerDay = float(varDict["cpPerDay"])
            self.m.cpPerBox = float(varDict["cpPerBox"])
            self.m.cpIncome = float(varDict["cpIncome"])
            self.m.database.newLog(log=self.m.logMed(newMed="y"))

    def dataView(self):
        fullLogs = self.m.database.loadLogsFull()
        fullDict = {}
        for x in fullLogs:
            for z, y in x.items():
                fullDict[z] = y
        df = pd.DataFrame(fullDict, columns=[
            "id", "name", "time", "intake", 'income', "storageToday", "nextBuyDate"])
        print(df)

    def menuSelection(self):
        select = self.start()
        while select != "":
            if select == 1:
                self.update()
                break
            elif select == 2:
                self.newData()
                break
            elif select == 3:
                break

        if select == "":
            print("See yout next time!")
        else:
            self.menuSelection()

    def mainUpdate(self):
        # lista de nomes
        nameList = self.m.database.loadNameList()
        dateControl = {}
        for name in nameList:
            lastLog = self.m.database.loadLastLogs(med=name)
            self.m.name = lastLog.get("name")
            self.m.intake = lastLog.get("intake")
            self.m.income = 0
            buyDate = self.m.nextBuyDate()
            self.m.database.newLog(log=self.m.logMed(newMed="n"))
            dateControl.update({self.m.name: buyDate})

        for x, y in dateControl.items():
            delta = td(days=y)
            today = dt.now()
            if today + delta >= 7:
                self.t.show_toast(title="--Medication shopping alert---",
                                  msg="{} storage end in less than a week}".format(x),
                                  threaded=True,
                                  duration=5)
            else:
                continue


###########################################################################################################


mm = MainMeds()
# mm.menuSelection()
mm.mainUpdate()
