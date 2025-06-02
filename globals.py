from datetime import datetime as DateTime
import jsonschema
from tzlocal import get_localzone

def sign(n):
    if n < 0:
        return -1
    else:
        return 1

aPP = [
PayPeriod(1, DateTime(2020, 12,  1,  0,  1, 0), DateTime(2020, 12, 14, 23, 59, 0)),
PayPeriod(2, DateTime(2020, 12, 15,  0,  1, 0), DateTime(2020, 12, 28, 23, 59, 0))
]
allPayPeriods = tuple(aPP)
del aPP
# enforce constraints (unique, etc.)

def get_property_values(T, P):
    return [getattr(obj, P, None) for obj in T if hasattr(obj, P)]

# get_property_values(allPayPeriods, "uid") # [1, 2]

#                 whichHour:employeeID
hoursInPayPeriod = {"Sun_0":0,
"Sun_1":0,
"Sun_2":0,
"Sun_3":0,
"Sun_4":0,
"Sun_5":0,
"Sun_6":0,
"Sun_7":0,
"Sun_8":0,
"Sun_9":0,
"Sun_10":0,
"Sun_11":0,
"Sun_12":0,
"Sun_13":0,
"Sun_14":0,
"Sun_15":0,
"Sun_16":0,
"Sun_17":0,
"Sun_18":0,
"Sun_19":0,
"Sun_20":0,
"Sun_21":0,
"Sun_22":0,
"Sun_23":0,
"Mon_0":0,
"Mon_1":0,
"Mon_2":0,
"Mon_3":0,
"Mon_4":0,
"Mon_5":0,
"Mon_6":0,
"Mon_7":0,
"Mon_8":0,
"Mon_9":0,
"Mon_10":0,
"Mon_11":0,
"Mon_12":0,
"Mon_13":0,
"Mon_14":0,
"Mon_15":0,
"Mon_16":0,
"Mon_17":0,
"Mon_18":0,
"Mon_19":0,
"Mon_20":0,
"Mon_21":0,
"Mon_22":0,
"Mon_23":0,
"Tue_0":0,
"Tue_1":0,
"Tue_2":0,
"Tue_3":0,
"Tue_4":0,
"Tue_5":0,
"Tue_6":0,
"Tue_7":0,
"Tue_8":0,
"Tue_9":0,
"Tue_10":0,
"Tue_11":0,
"Tue_12":0,
"Tue_13":0,
"Tue_14":0,
"Tue_15":0,
"Tue_16":0,
"Tue_17":0,
"Tue_18":0,
"Tue_19":0,
"Tue_20":0,
"Tue_21":0,
"Tue_22":0,
"Tue_23":0,
"Wed_0":0,
"Wed_1":0,
"Wed_2":0,
"Wed_3":0,
"Wed_4":0,
"Wed_5":0,
"Wed_6":0,
"Wed_7":0,
"Wed_8":0,
"Wed_9":0,
"Wed_10":0,
"Wed_11":0,
"Wed_12":0,
"Wed_13":0,
"Wed_14":0,
"Wed_15":0,
"Wed_16":0,
"Wed_17":0,
"Wed_18":0,
"Wed_19":0,
"Wed_20":0,
"Wed_21":0,
"Wed_22":0,
"Wed_23":0,
"Thu_0":0,
"Thu_1":0,
"Thu_2":0,
"Thu_3":0,
"Thu_4":0,
"Thu_5":0,
"Thu_6":0,
"Thu_7":0,
"Thu_8":0,
"Thu_9":0,
"Thu_10":0,
"Thu_11":0,
"Thu_12":0,
"Thu_13":0,
"Thu_14":0,
"Thu_15":0,
"Thu_16":0,
"Thu_17":0,
"Thu_18":0,
"Thu_19":0,
"Thu_20":0,
"Thu_21":0,
"Thu_22":0,
"Thu_23":0,
"Fri_0":0,
"Fri_1":0,
"Fri_2":0,
"Fri_3":0,
"Fri_4":0,
"Fri_5":0,
"Fri_6":0,
"Fri_7":0,
"Fri_8":0,
"Fri_9":0,
"Fri_10":0,
"Fri_11":0,
"Fri_12":0,
"Fri_13":0,
"Fri_14":0,
"Fri_15":0,
"Fri_16":0,
"Fri_17":0,
"Fri_18":0,
"Fri_19":0,
"Fri_20":0,
"Fri_21":0,
"Fri_22":0,
"Fri_23":0,
"Sat_0":0,
"Sat_1":0,
"Sat_2":0,
"Sat_3":0,
"Sat_4":0,
"Sat_5":0,
"Sat_6":0,
"Sat_7":0,
"Sat_8":0,
"Sat_9":0,
"Sat_10":0,
"Sat_11":0,
"Sat_12":0,
"Sat_13":0,
"Sat_14":0,
"Sat_15":0,
"Sat_16":0,
"Sat_17":0,
"Sat_18":0,
"Sat_19":0,
"Sat_20":0,
"Sat_21":0,
"Sat_22":0,
"Sat_23":0
}

# allEmployees = .




class scheduledHour:
    def __init__(self, h, pp, e):
        assert isinstance(h, LocalHour)
        assert isinstance(pp, PayPeriod)
        assert isinstance(e, Employee)
        self.dayOfWeekInteger = h.dayOfWeekInteger
        self.localHourInteger = h.hourInteger
        self.utcOffset = h.utcOffset



/*

'''

import jsonschema

# Define a JSON Schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0}
    },
    "required": ["name", "age"]
}

# Create a Python object (dictionary)
data = {"name": "Alice", "age": 25}

# Validate the object
jsonschema.validate(instance=data, schema=schema)

print("Validation successful!")




*/




{
"if":	{
		"anyOf":	[
					{
					"properties":	{
									"year": {"const":2025},
									"month": {"const":3},
									"dayOfMonth": {"minimum":9}
									}
					},
					{
					"properties":	{
									"year": {"const": 2025},
									"month": {"minimum":4, "maximum":10}
									}
					},
					{
					"properties":	{
									"year": {"const": 2025},
									"month": {"const": 11},
									"dayOfMonth": {"maximum":1}
									}
					}
					]
		},
"then":	{
		"properties":	{
						"utcOffset": {"const": -4}
						}
		},
"else":	{
		"properties":	{
						"utcOffset": {"const": -5}
						}
		}
}






'''




Timesheet
(must be only one timesheet per unique combo of (employeeID, payPeriodID)
id
employeeID foreign key 
payPeriodID foreign key
status (draft, submitted, withdrawn, approved)
hoursWorked = [hourID1, hourID2, etc.] # foreign keys

Hour
id (0-335)
utcOffset (e.g. -4)
hourInteger (0-23) # including minutes :00 thru :59
day (0-6)
shiftWhichThisHourWouldUsuallyBePartOf (id) # seems useful 

Shift
id
hourBeginInteger
hourOnTheStrikingOfWhichThisShiftEnds # intege





