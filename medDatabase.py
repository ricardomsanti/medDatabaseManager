from datetime import datetime as dt
from datetime import timedelta as dt
from datetime import timezone as tm
tm.utc
from pymongo import MongoClient

#--------------------------------------missing implementing mongo db methods

class MedDatabase:
    
    def __init__(self, client, db, col):
        self.client = MongoClient("localhost", 2707), 
        self.db = client.get_database("meds"), 
        self.col = db.get_collection("medLogs")
    
                
        
    
    
                            
     
    def findStorage(self, field):
        log_list = self.col.find({},{field : 1})
        for log in log_list:
            print(log)
    
    
    def __init__(self, boxNum):
        self.boxNum = boxNum
        
    def med_log(self, name, boxNum):
        pass
        
    def total(self, boxNum, laststorage):
        full_storage = laststorage
        full_storage += boxNum
        return full_storage
            
 
    
 
