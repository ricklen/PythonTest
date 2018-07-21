# Create a program that allows a user to choose one of 
# up to 9 time zones from a menu. You can choose any
# zones you want from all the all_timezones list.
#
# The program will then display the time in that timezone, as well
# as the local time and the utc time.
# 
# Entering 0 as a choice will quit the program.
# 
# Display the dates and time in a format suitable for the 
# user of your program to understand, and include the timezone 
# name when displaying the chosen time.


import datetime
import pytz


countryList = ['Europe/Amsterdam', 'America/Matamoros', 'Africa/Bamako', 'Europe/Skopje' 
                                , 'Pacific/Kwajalein', 'Europe/Podgorica', 'Pacific/Guam'
                                ,  'Africa/Conakry', 'Africa/Accra']

answer = int

def printCountrylist():
    for i in range(0,len(countryList)):
        print("{} : {}".format(i + 1, countryList[i]))

def askQuestion():
    global answer
    question = input("Select one of the countries above by entering a number up to 9: ")
    answer = int(question)

while answer != 0:
    printCountrylist()
    askQuestion()
    print("Selected timezone is {}".format(countryList[answer - 1]))
    print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
    print("{} time is {}".format(countryList[answer - 1],datetime.datetime.now(tz=pytz.timezone(countryList[answer - 1])).strftime('%A %x %X')))
    print("local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))

