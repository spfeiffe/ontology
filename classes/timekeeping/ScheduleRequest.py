class ScheduleRequest:
    def __init__(self, id, pp, h, e):
        self.id = id
        if pp not in get_property_values(allPayPeriods, "uid"):
            raise Exception("ScheduleRequest.pp must be in get_property_values(allPayPeriods, 'uid')")
        self.pp = pp
        if type(h) is not list:
            if type(h) is not str:
                raise Exception("ScheduleRequest.h must be either a list or a string")
            if h not in hoursInPayPeriod:
                raise Exception("ScheduleRequest.h[0] must be in the Schedule for PayPeriod[id=pp].")
        for i in range(len(h)):
            if h[i] not in hoursInPayPeriod:
                raise Exception("ScheduleRequest.h[" + str(i) + "] must be in the Schedule for PayPeriod[id=pp].")
        self.h = h
        if e not in get_property_values(allEmployees, "uid"):
            raiseException('ScheduleRequest.e must be in get_property_values(allEmployees, "uid")')
        self.e = e
        self.status = "draft" # ["draft", "submitted", "approved", "denied", "withdrawn"] 
        self.reasonDenied = None # must be not None if self.status = "denied"
    
    def fulfill(self):
        # if self.status == "approved":
        #   # thisSchedule = get instance of `Schedule` with pay period id = self.pp
        #   #
        #   # thisSchedule.[self.h] = self.e
