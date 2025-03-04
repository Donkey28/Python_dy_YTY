s = input()
num = s.split()
x = int(num[0])
y = int(num[1])

if -1 <= x <= 1 and -1 <= y <= 1:
    print('yes')
else:
    print('no')