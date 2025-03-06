n, m, k = map(int, input().split())

# 读取矩阵 A
A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# 读取矩阵 B
B = []
for _ in range(m):
    row = list(map(int, input().split()))
    B.append(row)

# 初始化矩阵 C
C = [[0] * k for _ in range(n)]

# 计算矩阵乘法
for i in range(n):
    for j in range(k):
        for l in range(m):
            C[i][j] += A[i][l] * B[l][j]

# 输出矩阵 C
for row in C:
    print(" ".join(map(str, row)))

