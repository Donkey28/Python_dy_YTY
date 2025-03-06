import re
# 定义正则表达式，用于匹配非负整数和小数
m = r'\d+(\.\d+)?'
while True:
    try:
        s = input()
        lst = re.findall(m, s)
        for x in lst:
            if isinstance(x, tuple):
                # 若匹配结果是元组，将元组元素拼接成字符串
                print(''.join(x))
            else:
                print(x)
    except:
        break