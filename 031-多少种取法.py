def ways(m, n, s):
    if n == 0 and s == 0:
        return 1
    if m < 1 or n < 0 or s < 0:
        return 0
    return ways(m - 1, n - 1, s - m) + ways(m - 1, n, s)

t = int(input())
for _ in range(t):
    m, n, s = map(int, input().split())
    print(ways(m, n, s))