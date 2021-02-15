import pandas as pd

from Med import Med as m


class MainMeds:
    dash = "================================================================================================"

    

    def start(self):

        print(self.dash)
        print()
        print("MainMeds started")
        print()
        print(self.dash)

    def menuSelection(self):
        # ----------------------------------------------refine this dataFrame

        OpList = ["Log medication", "View graphics", "Add new drugs"]
        menuSeries = pd.Series(OpList, index={1,2,3})        
        print(menuSeries)
        select = input("Please choose an option from the menu \n")
        while select != "":
            select = int(select)
            if select == 1:
                # ------------------------------------------------------------------------------------
                pass
                """print("Please choose a medication to update from the list")
                medList = set(MedDatabase.findStorage("name"))
                """
            elif select == 2:
                # ------------------------------------------------------------------------------------
                pass
            elif select == 3:
                # ------------------------------------------------------------------------------------
                confirm = ""
                next = ""
                while confirm == "":
                    print("Please type the following data about the new medication \n")
                    varList = ["name",
                            "dosePerDay",
                            "cpPerDay",
                            "cpPerBox",
                            "pricePerBox",
                            "cpPerBuy"]
                    varDict = {}
                    for x in varList:
                        value = input("{}: \n".format(x))
                        varDict.update({str(x): value})
                    next = input("-----------------------------------Log med?[y/n]\n")
                    if next == "y":
                    
                        # New instance of MainMeds
                        m.name=varDict["name"],
                        m.cpdosePerDay=float(varDict["dosePerDay"])
                        m.cpPerDay=float(varDict["cpPerDay"])
                        m.cpPerBox=float(varDict["cpPerBox"])
                        m.pricePerBox=float(varDict["pricePerBox"])
                        m.cpIncome=float(varDict["cpPerBuy"])
                        
                        m.logInsert_Med()
                    else:
                        continue


###########################################################################################################


# create
# selectbox
# update
# delete


mm = MainMeds()
mm.start()
mm.menuSelection()
