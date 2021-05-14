#! /usr/bin/env python3
  
#
#Julian Day
#
#25April20


import time

def whodatboi(usrDate):
    usrinput = time.strptime(usrDate, "%d%b%Y")
    lst = []
    lst.append(usrinput.tm_year)
    lst.append(usrinput.tm_mon)
    lst.append(usrinput.tm_mday)
    return lst

#function below defined in handout
def julianday(year, month, day):
    if month ==1 or month ==2:
        year -=1
        month +=12
    if month >2:
        year = year
        month = month
    if year >= 1582:
        A = int(year/100)
        B = 2 - A + int(A/4)

    else:
        B = 0

    JD = int((365.25 * (year + 4716)) + int(30.6001 * (month +1)) + day + B - 1524.5)
    return JD


Date = input('Enter the Date in Format DDMmmYYYY:')
lstparts = whodatboi(Date)
print()
jday = julianday(lstparts[0],lstparts[1],lstparts[2])
print('The Julian Day Number is : '+str(jday))
wkday = (int)(jday+1)%7
print()
a = time.gmtime()
b = julianday(a.tm_year,a.tm_mon,a.tm_mday)

print('The Week Day Number is: '+str(wkday))
print()
print('The Age in Days is: '+str((int)(b-jday)))
print()
