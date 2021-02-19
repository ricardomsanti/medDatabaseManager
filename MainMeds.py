import pandas as pd
from MedOps import MedOps as mo
from Med import Med as m
from MedDatabase import MedDatabase as md
from pymongo import MongoClient


class MainMeds:
    def __init__(self):
        self.MedOps = mo()

    dash = "================================================================================================"

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

    def menuSelection(self):
        select = self.start()
        while select != "":
            if select == "1":
                # ------------------------------------------------------------------------------------
                nameList = self.MedOps.database.loadNameList()
                nameSeries = pd.Series(nameList, index=[1,2,3,4,5])
                print(nameSeries.to_string())
                medName = input("Please choose a medication to update from the list \n")
                print(self.dash)
                print()
                lastLog = [dict(x) for x in self.MedOps.database.loadLastLogs(med=medName)]
                print("Last log data retrieved successflly. \n Please type in a new value in case of update, \n"
                      "or just hit enter for the next item \n")
                print(self.dash)
                print()
                newLog = {}
                for z in lastLog:
                    for x, y in z.items():
                        value = input("Field: {}    Current value: {} \n".format(x, y))
                        if y == "":
                            newLog[str(x)] = {value}
                        else:
                            newLog[str(x)] = {y}
                    for x, y in newLog.items():
                        print(x, y)

                break

            elif select == 2:
                # ------------------------------------------------------------------------------------

                print("Please type the following data about the new medication \n")
                varList = ["name",
                           "cpPerDay",
                           "cpPerBox",
                           "cpIncome"]
                varDict = {}
                for x in varList:
                    value = input("{}: \n".format(x))
                    varDict.update({str(x): value})
                next = input("-----------------------------------Log med?[y/n]\n")
                if next == "y":

                    self.MedOps.med.name = varDict["name"],
                    self.MedOps.med.cpPerDay = float(varDict["cpPerDay"])
                    self.MedOps.med.cpPerBox = float(varDict["cpPerBox"])
                    self.MedOps.med.cpIncome = float(varDict["cpIncome"])
                    self.MedOps.database.newLog(log=self.MedOps.logMed())
                else:
                    break
            elif select == 3:
                fullLogs = self.MedOps.database.loadLogsFull()
                fullDict = {}
                for x in fullLogs:
                    for z, y in x.items():
                        fullDict[z] = y
                df = pd.DataFrame(fullDict, index=[x for x in range(len(fullDict)-1)])
                print(df)
                break

        self.menuSelection()








###########################################################################################################


mm = MainMeds()
mm.menuSelection()
