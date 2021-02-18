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
        nameList = [post["name"] for post in self.col.find()]
        return list(set(nameList))

    def loadLogsMed(self, med):
        # queries the database returning only the logs which math a certain name
        logs = self.loadLogsFull()
        logsMed = [post for post in logs if post["name"] == med]
        return logsMed

    def loadLastLogs(self, med):
        # queries the database returning only the last logged log
        logs = self.loadLogsMed(med=med)
        selectLogList = [post for post in logs[(len(logs) - int(1)): len(logs)]]
        return selectLogList



m = MedDatabase().loadNameList()
for x in m:
    print(x)