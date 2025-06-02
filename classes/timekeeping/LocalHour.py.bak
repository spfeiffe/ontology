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
