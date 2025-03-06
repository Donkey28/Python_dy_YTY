def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
# 获取每个月的天数
def get_days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days[1] = 29
    return days[month - 1]


def days_since_0(year, month, day):
    total_days = 0
    if year == 0:# 公元0年情况
        for m in range(1,month):
            total_days += get_days_in_month(year,m)
        total_days += day - 1

    elif year > 0:# 公元大于0年份情况
        for y in range(0,year):
            if is_leap_year(y) :
                total_days += 366
            else:
                total_days += 365
        for m in range(1,month):
            total_days += get_days_in_month(year,m)
        total_days += day - 1

    elif year < 0:# 公元小于0年份情况
        # total_days += days_since_0(2020,11,18)
        for y in range(1,-year):
            if is_leap_year(y):
                total_days += 366
            else:
                total_days += 365
        for m in range(1,month):
            total_days -= get_days_in_month(-year,m)
        total_days -= day - 1 
        if is_leap_year(-year):
            total_days += 366
        else:
            total_days += 365
    print(total_days)
    return total_days


y = int(input())
m = int(input())
d = int(input())

days_since_0(y,m,d)
# days_since_0(2020,11,18)