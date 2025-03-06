n = int(input())
# 读取向量 a 的元素
a = list(map(int, input().split()))
# 读取向量 b 的元素
b = list(map(int, input().split()))

dot_product = 0
# 计算点积
for i in range(n):
    dot_product += a[i] * b[i]

print(dot_product)
