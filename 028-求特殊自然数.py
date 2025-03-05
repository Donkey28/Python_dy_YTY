i = 0
while True:
    if (i % 81 // 9 == i % 49 // 7) and (i % 9 == i // 49) and (i // 81 == i % 7) and (i != 0):

        break
    else:
        i += 1
print(i)
print(i // 49 * 100 + i % 49 // 7 * 10 + i % 7)
print(i // 81 * 100 + i % 81 // 9 * 10 + i % 9)
# 注意题目要求最终输出三行，分别是十进制、七进制、九进制