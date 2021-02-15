from pymongo import MongoClient


# --------------------------------------missing implementing mongo db methods


class MedDatabase:

    def __init__(self, client, db, col):
        self.client = client
        self.db = db
        self.col = col

    def logInsert(self, log):
        try:
            self.col.insert_one(log)
        except:
            print("Sorry, it was not possible to log this data to medLogs collection")


    #working database method, altough it needs some fixex about instantiating or no the MongoClient on the def __init__

    #still neet to be able to execise QUERYNG operators and EXTRACTING values from BSON to Python Objects

    #once all that is done, it's only a matter of formating the calculation, and displaying results using pandas
    def loadLogs(self):
        loadLogs = {}
        loadList = []

        for x in self.col.find():
            loadList.append(x)
            print(x)





client = MongoClient("localhost", 27017)
db = client.get_database("MEDS")
col = db.get_collection("medLog")
MedDatabase(client=client, db=db, col=col).loadLogs()
