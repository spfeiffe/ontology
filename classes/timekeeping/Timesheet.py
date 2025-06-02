class Timesheet:# Schedule = hours planned to work; Timesheet = hours actually worked. 
    def __init__(self, id, employeeId, payPeriodId, h):
        # must be only one timesheet per unique combo of (employeeID, payPeriodID) 
        self.id = id
        self.eid = employeeId
        self.ppid = payPeriodId
        if type(h) is not list:
            raise Exception("Timesheet.h must be of type `list`, even if it is of len=0 or len=1.") 
        self.h = h
