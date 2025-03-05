s = input().split()
L,R = int(s[0]),int(s[1])
total = 0
for i in range(L,R+1):
    st = str(i)
    for i in range(len(st)):
        if st[i] == '2':
            total += 1   
print(total)