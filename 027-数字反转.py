n = int(input())

if n == 0:
    print(0)
elif n > 0:
    st = str(n)
    # 反转字符串并去除前导零
    result = st[::-1].lstrip('0')
    print(result if result else '0')
else:
    # 处理负数情况
    st = str(-n)
    result = st[::-1].lstrip('0')
    print('-' + result if result else '0')