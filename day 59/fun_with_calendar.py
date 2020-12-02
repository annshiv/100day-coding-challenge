import calendar

def check_vaild_date(d,m,y,l):
    day_31 = [1,3,5,7,8,10,12]
    day_30 = [4,6,11,9]
    if d > 0 and d < 32:
        if l:
            if m == 2:
                if d < 30:
                    return True
                else:
                    return False
         
            else:
                if m in day_30:
                    if d > 30:
                        return False
                    else:
                        return True
                elif m in day_31:
                    if d > 31:
                        return False
                    else:
                        return True

        else:
            if m == 2:
                if d < 29:
                    return True
                else:
                    return False
            else:
                if m in day_30:
                    if d > 30:
                        return False
                    else:
                        return True
                elif m in day_31:
                    if d > 31:
                        return False
                    else:
                        return True
    else:
        return False

def check_leap(year):
    if (year % 4 == 0) or (year % 100 == 0 and year % 400 ==0):
        return True
    else:
        False


while(1):
    year = int(input("Enter year (from 1970) : "))

    if year<1970:
        print("Enter a year starting from 1970")

    else:
        break

while(1):
    month = int(input("Enter month (1 - 12) : "))

    if month > 1 and month <= 12:
        break
    else:
        print("Enter a valid month (1-12)")

leap = check_leap(year)

while(1):
    date = int(input("Enter date : "))

    if check_vaild_date(date,month,year,leap):
        break
    else:
        print("Enter a valid date")

day_index = calendar.weekday(year,month,date)
list_of_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
day = list_of_days[day_index]
print(str(date) + "-" + str(month) + "-" + str(year) + " falls on " + day )