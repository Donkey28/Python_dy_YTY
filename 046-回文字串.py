s = input()
result = []

# 遍历所有可能的子串长度
for length in range(2, len(s) + 1):
    # 遍历所有可能的起始位置
    for start in range(len(s) - length + 1):
        end = start + length
        sub_str = s[start:end]
        # 判断子串是否为回文串
        if sub_str == sub_str[::-1]:
            result.append(sub_str)

# 输出结果
for sub_str in result:
    print(sub_str)

