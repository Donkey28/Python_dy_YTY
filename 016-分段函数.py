s = float(input())
if 0 <= s < 5:
    print(format(-s + 2.5, '.3f'))
elif 5 <= s < 10:
    print(format(2 - 1.5 * (s - 3) * (s - 3)  ,'.3f'))
else:
    print(format(s / 2 - 1.5,'.3f'))
