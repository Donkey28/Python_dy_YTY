S, S1, S2 = input().split(',')

# 查找 S1 第一次出现的结束位置
first_S1_end = S.find(S1)
if first_S1_end != -1:
    first_S1_end += len(S1)

# 查找 S2 最后一次出现的开始位置
last_S2_start = S.rfind(S2)

# 检查是否满足条件
if first_S1_end != -1 and last_S2_start != -1 and first_S1_end <= last_S2_start:
    span = last_S2_start - first_S1_end
    print(span)
else:
    print(-1)
