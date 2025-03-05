s = input().split()
a = int(s[0])
b = int(s[1])
n = 1
total = []
while True:
    if a % n == 0 and b % n == 0:
        total.append(n)
        n += 1
        if n == a + 1 or n == b + 1:
            break
    else:
        n += 1
        if n == a + 1 or n == b + 1:
            break
print(max(total))
