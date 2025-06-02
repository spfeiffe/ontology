class LocalHour:
    def __init__(self, dayOfWeekInteger, hourInteger, utcOffset):
        self.classType = "timekeeping"
        self.dayOfWeekInteger = dayOfWeekInteger
        self.hourInteger = hourInteger
        self.utcOffset = utcOffset
    
    def getUtcHour(self):
        localDayOfWeekInteger = self.dayOfWeekInteger
        localHourInteger = self.hourInteger
        utcHourIntegerRAW = localHourInteger - (sign(self.utcOffset) * self.utcOffset)
        if utcHourIntegerRAW < 0:
            utcDayOfWeekInteger = ((localDayOfWeekInteger - 1) % 7)
        elif utcHourIntegerRAW > 23:
            utcDayOfWeekInteger = ((localDayOfWeekInteger + 1) % 7)
        else:
            utcDayOfWeekInteger = localDayOfWeekInteger
        utcHourInteger = (utcHourIntegerRAW % 24)
        return UtcHour(utcDayOfWeekInteger, utcHourInteger)

'''
a = []
now = DateTime.now(get_localzone())
currentUtcOffset = int(now.utcoffset().total_seconds() / 3600)
for dayInt in range(7):
    for h in range(24):
        a.append( LocalHour(dayInt, h, currentUtcOffset) )

allLocalHours = tuple(a)
del a

l = allLocalHours[24]
l.dayOfWeekInteger
l.hourInteger
l.utcOffset
l.getUtcHour().dayOfWeekInteger
l.getUtcHour().hourInteger

l = allLocalHours[23]
l.dayOfWeekInteger
l.hourInteger
l.utcOffset
l.getUtcHour().dayOfWeekInteger
l.getUtcHour().hourInteger

l = LocalHour(0, 3, 6)
l.dayOfWeekInteger
l.hourInteger
l.utcOffset
l.getUtcHour().dayOfWeekInteger
l.getUtcHour().hourInteger
'''
