import bson
from pymongo import MongoClient


# Resposible for instatiating the database, as well as loggin ant retrieving data from it


class MedDatabase:

    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.get_database("MEDS")
        self.col = self.db.get_collection("medLog")

    def newLog(self, log):
        self.col.insert_one(log)
        print("Log operation succesfully performed")

    def loadLogsFull(self):
        loadLogs = []
        posts = self.col.find()
        for post in posts:
            loadLogs.append(dict(post))
        return loadLogs

    def loadNameList(self):
        # queries the database returning only medication names
        nameList = []
        for x in self.loadLogsFull():
            for z, y in x.items():
                if z == "name" and y not in nameList:
                    nameList.append(y)
                else:
                    continue
        return nameList

    ##Find out how to use a variable that has been declared in the upper class
    ##Research in the python folders
    ##def loadLogsMed(self, med):

    def loadLastLogs(self, med):
        logs = self.loadLogsFull()
        logMed = [post for post in logs if post["name"] == med]
        # queries the database returning only the last logged log
        lastLog = logMed[int(len(logMed)-1)]
        return lastLog


