#doomsday.py

import datevalidator as dv

daysofweek = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

def isleapyear(year):
    if year % 100 == 0:
        return (year % 4 == 0 and year % 400 == 0)
    elif year % 4 == 0:
        return True
    return False

def getdoomsdays(year):
    leapdoomsdays = {1:4, 2:29, 3:7, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}
    doomsdays = {1:3, 2:28, 3:7, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}
    if isleapyear(year):
        return leapdoomsdays
    return doomsdays

def doomdif(day, month, year):
    doomsdays = getdoomsdays(year)
    doomsdaydate = doomsdays[month]
    daydif = abs(doomsdaydate - day)
    return daydif

def anchor(year):
#used for fidning doomsday
#returns the anchor of the year
#the algorithmic method of getting the anchor can return 0, 1, 2, 3 which corresponds with
#Tuesday, Sunday, Friday, and Wednesday as anchor days. The key in the results dictionary is what
#r is equal to, and the value stored at that key is the key for that day of week in the daysofweek dictionary
    results = {0:2, 1:0, 2:5, 3:3}
    r = (year//100) % 4
    return results[r]

def doomsday(year, anchor):
    #dow that the doomsdays are
    halfyear = year - ((year//100) * 100)
    fit = halfyear // 12
    difference = abs(halfyear - (fit * 12))
    fit2 = difference // 4
    total = anchor + fit + difference + fit2
    return total - (7 * (total // 7))

def extractdate(date):
    month, day, year = date.split('/')
    month, day, year = int(month), int(day), int(year)
    return day, month, year

def finddow(doomdif, doomsday):
    count = doomdif
    pos = doomsday
    for i in range(count):
        pos += 1
        if pos == 7:
            pos = 0
        dow = daysofweek[pos]
    return pos  


def main(date):
    day, month, year = extractdate(date)
    if dv.is_valid_date(day, month, year):
        daydif = doomdif(day, month, year)
        anch = anchor(year)
        doom = doomsday(year, anch)
        dow = finddow(daydif, doom)
        return daysofweek[dow]
    else:
        return False
