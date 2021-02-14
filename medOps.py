class MedOps:
            
    def __init__(self, timeZero, timeOne, sizeZero, sizeOne, intake):
        self.timeZero = timeZero, 
        self.timeOne = timeOne, 
        self.sizeZero = sizeZero, 
        self.sizeOne = sizeOne
        self.intake = intake
        
    
        
    # deltas    
    #-----------------------------------------------------------------------------
    def deltaMain(self):
        
        result = 0
        
        #TIME OF THE LAST MEDICATION SHOP
        if self.timeZero == None:
            self.timeZero = ((self.sizeOne -self.sizeZero)/self.intake)+ self.timeOne
            result = self.timeZero
        #TIME OF THE NEXT MEDICATION SHOP
        elif self.timeOne == None:
            delta_size = self.sizeOne - self.sizeZero
            timeOne = self.timeZero - (self.sizeOne -self.sizeZero)/self.intake
            result = self.timeOne
        #MEDICATION STORAGE AT A PAST DATE
        elif self.sizeZero == None:
            sizeZero = ((self.timeOne -self.timeZero)/self.intake) + self.sizeOne 
            result = sizeZero
        #MEDICATION STORAGE AT A FUTURE TIME
        elif self.sizeOne == None:
            sizeOne = self.sizeZero - ((self.timeOne -self.timeZero)/self.intake)
            result = sizeOne
        
        return result        
    
    
    # isolated varables
    #---------------------------------------------------------------------
    
    def find_intake(self, size, time):
        intake = lambda size , time : size/time
        return intake(size, time)
    
    def find_size(self, intake, time):
        size = lambda intake, time: intake/time
        return size
    def find_time(self, intake, size):
        time = lambda intake, size : intake/size
        return time
 
        
