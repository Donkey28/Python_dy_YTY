s = input()
str = s.split()
n = 0
for i in range(len(str)):
    for j in range(len(str[i])):
        if ord(str[i][j]) in range(48,58):
            n += 1
print(n)