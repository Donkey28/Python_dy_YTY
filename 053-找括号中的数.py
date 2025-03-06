import re

n = int(input())
for _ in range(n):
    s = input()
    # 正则表达式匹配符合条件的整数
    pattern = r'<([1-9]\d{0,2}|0)>'
    result = re.findall(pattern, s)
    if result:
        print(" ".join(result))
    else:
        print("NONE")
