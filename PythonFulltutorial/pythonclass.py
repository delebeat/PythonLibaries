class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

currentTime = Time(9, 14, 30)
currentTime.printTime()
