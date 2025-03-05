s = input()
lst = s.split()
a = int(lst[0])
b = int(lst[1])
cau = lst[2]
if cau == '+':
    print(a + b)
elif cau == '-':
    print(a - b)
elif cau == '*':
    print(a * b)
elif cau == '/':
    if b == 0:
        print('Divided by zero!')
    else:
        print(int(a / b))
else:
    print('Invalid operator!')