

class MedOps:


    t0 = 0.0
    t1 = 0.0
    def __init__(self, timeZero, t1, s0, s1, intake):
        self.t0 = timeZero,
        self.t1 = t1,
        self.s0 = s0,
        self.s1 = s1

        self.intake = intake

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
