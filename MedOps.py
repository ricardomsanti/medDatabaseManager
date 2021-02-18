from MedDatabase import MedDatabase as md
from Med import Med as m

#Responsible for instatiating the Med Class as well as the MedDatabase and performing the necessary calculation so new logs can be mande

class MedOps:

    def __init__(self):
        self.database = md()
        self.med = m()

    # deltas

    # -----------------------------------------------------------------------------
    def deltaMain(self):

        result = 0

        # TIME OF THE LAST MEDICATION SHOP
        if self.t0 == None:
            self.t0 = ((self.s1 - self.s0) / self.intake) + self.t1
            result = self.t0
        # TIME OF THE NEXT MEDICATION SHOP
        elif self.t1 is None:
            result = self.t0 - (self.s1 - self.s0) / self.intake

        # MEDICATION STORAGE AT A PAST DATE
        elif self.s0 is None:
            s0 = ((self.t1 - self.t0) / self.intake) + self.s1
            result = s0
        # MEDICATION STORAGE AT A FUTURE TIME
        elif self.s1 is None:
            s1 = self.s0 - ((self.t1 - self.t0) / self.intake)
            result = s1

        return result

        # isolated varables

    # ---------------------------------------------------------------------

    def find_intake(self, size, time):
        intake = lambda size, time: size / time
        return intake(size, time)

    def find_size(self, intake, time):
        size = lambda intake, time: intake / time
        return size

    def find_time(self, intake, size):
        time = lambda intake, size: intake / size
        return time
