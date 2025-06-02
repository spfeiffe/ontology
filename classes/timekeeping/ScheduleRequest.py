class ScheduleRequest:
    def __init__(self, pp, h, e):
        if pp not in get_property_values(allPayPeriods, "uid"):
            raise Exception("ScheduleRequest.pp must be in get_property_values(allPayPeriods, 'uid')")
        self.pp = pp
        if type(h) is not list:
            if type(h) is not str:
                raise Exception("ScheduleRequest.h must be either a list or a string")
            if h not in hoursInPayPeriod:
                raise Exception("ScheduleRequest.h[0] must be in `hoursInPayPeriod`")
        for i in range(len(h)):
            if h[i] not in hoursInPayPeriod:
                raise Exception("ScheduleRequest.h[" + str(i) + "] must be in `hoursInPayPeriod`")
        self.h = h
        if e not in get_property_values(allEmployees, "uid"):
            raiseException('ScheduleRequest.e must be in get_property_values(allEmployees, "uid")')
        self.e = e
        self.status = "draft" # ["draft", "submitted", "approved", "denied"]
        self.reasonDenied = None # must be not None if self.status = "denied"
