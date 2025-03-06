N, NA, NB = map(int, input().split())
A_pattern = list(map(int, input().split()))
B_pattern = list(map(int, input().split()))
A_wins = 0
B_wins = 0

for i in range(N):
    # 计算当前轮次 A 和 B 的出拳
    A_choice = A_pattern[i % NA]
    B_choice = B_pattern[i % NB]

    # 判断胜负
    if (A_choice == 0 and B_choice == 2) or (A_choice == 2 and B_choice == 5) or (A_choice == 5 and B_choice == 0):
        A_wins += 1
    elif (B_choice == 0 and A_choice == 2) or (B_choice == 2 and A_choice == 5) or (B_choice == 5 and A_choice == 0):
        B_wins += 1

# 输出结果
if A_wins > B_wins:
    print("A")
elif B_wins > A_wins:
    print("B")
else:
    print("draw")

