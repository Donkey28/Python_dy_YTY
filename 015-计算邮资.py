s1 = input()
s = s1.split()
a = int(s[0])
b = s[1]
fast = 0
n = 0
if a <= 1000:
    if b == 'y':
        fast = 1
    elif b =='n':
        fast = 0
elif a > 1000:
    if a % 500 == 0:
        n = (a - 1000) / 500
        if b == 'y':
            fast = 1
        elif b =='n':
            fast = 0
    else:
        n = (a - 1000) // 500 + 1
        if b == 'y':
            fast = 1
        elif b =='n':
            fast = 0

print(8 + 4 * n + 5 * fast)