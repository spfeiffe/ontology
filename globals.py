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

# allEmployees = .





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





