n = int(input())
for _ in range(n):
    s1, s2 = input().split()
    result = []
    index = 0
    while True:
        # 查找 s2 在 s1 中从 index 开始的位置
        found_index = s1.find(s2, index)
        if found_index == -1:
            break
        result.append(found_index)
        # 为避免重叠，更新查找的起始位置为当前找到位置加上 s2 的长度
        index = found_index + len(s2)
    if result:
        print(" ".join(map(str, result)))
    else:
        print("no")
