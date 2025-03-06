# 判断是否为闰年
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

# 计算从公元 0 年 1 月 1 日到指定日期的总天数
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
    # print(total_days)
    return total_days

# 判断日期是否合法
def is_valid_date(year, month, day):
    if month < 1 or month > 12:
        return False
    if day < 1 or day > get_days_in_month(year, month):
        return False
    return True

# 星期几的名称列表
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# 已知日期 2020 年 11 月 18 日是星期三
known_date = days_since_0(2020, 11, 18)
known_weekday = 3

years = []
months = []
days = []

n = int(input())
for _ in range(n):
    y, m, d = map(int, input().split())
    
    # 将年月日信息添加到列表管理，方便一起输出
    years.append(y)
    months.append(m)
    days.append(d)
for i in range(n):
    if not is_valid_date(y, m, d):
        print("Illegal")
    else:
        if y >= 0 and days_since_0(years[i],months[i],days[i]) <= known_date:
            days_diff = days_since_0(years[i],months[i],days[i]) - known_date
            weekday = (days_diff + known_weekday) % 7
            print(weekdays[weekday])
        elif y >= 0 and days_since_0(years[i],months[i],days[i]) > known_date:
            days_diff = days_since_0(years[i],months[i],days[i]) - known_date
            weekday = (days_diff + known_weekday) % 7
            print(weekdays[weekday])
        elif y < 0:
            days_diff = days_since_0(years[i],months[i],days[i])
            weekday = (days_diff - 1) % 7
            print(days_diff)
            print(weekdays[weekday])

    