from pymongo import MongoClient
from med import Med as m
from medOps import MedOps as mo
from medDatabase import MedDatabase as md   

import pandas as pd


###########################################################################################################





class MainMeds:
    dash = "================================================================================================"
    
    def __init__(self):
        pass

            
    def start(self):
        
        print(self.dash)
        print()
        print("MainMeds started")
        print()
        print(self.dash)
        
        
    def menuSelection(self):
        #----------------------------------------------refine this dataFrame
        
        menuOpList = ["Log medication", "View graphics", "Add new drugs"]
        numList = [1,2,3]
        menuOpDf = pd.DataFrame(menuOpList, index=numList)
        print("Please choose an option from the menu \n")
        print(menuOpDf)
        select = input()
        return select
    
    
    def ops(self, menuSelection):
        op = int(menuSelection)
        if op == 1:
            #------------------------------------------------------------------------------------
            pass
            """print("Please choose a medication to update from the list")
            medList = set(MedDatabase.findStorage("name"))
            """
        elif op == 2:
            #------------------------------------------------------------------------------------
            pass
        elif op == 3:
            #------------------------------------------------------------------------------------
            confirm = ""
            next = ""
            while confirm == "":
                print("Please type the following data about the new medication \n")
                varList = ["name",
                        "dosePerDay",
                        "cpPerDay",
                        "cpBox",
                        "boxPrice",
                        "cpNum"]
                varDict = {}
                for x in varList:
                    value = input("{}: \n".format(x))
                    varDict.update({str(x): value})
                next = input("-----------------------------------Log med?[y/n]\n")    
                if next == "y":
            #New instance of MainMeds
                    m(name=varDict["name"], dosePerDay=float(varDict["dosePerDay"]), cpPerDay=float(varDict["cpPerDay"]),
                            cpBox=float(varDict["cpBox"]), boxPrice=float(varDict["boxPrice"]), cpNum=float(varDict["cpNum"])).logMed()
                    
                    print("Medication log performed successfully")
                    break
                else:
                    print("Sorry something went wrong, please try aganin")
                    confirm == ""
                    
                
            
            
            

            
###########################################################################################################


#create
#selectbox
#update
#delete


mm = MainMeds()
mm.start()
mm.ops(mm.menuSelection())
