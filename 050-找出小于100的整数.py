import re
m = r"(^|[^0-9-])(\d{1,2})([^0-9]|$)"
for i in range(2):
    s = input()
    lst = re.findall(m, s)
    for x in lst:
        num = int(x[1])
        if 0 <= num < 100:
            print(num)
