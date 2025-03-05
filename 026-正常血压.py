time = int(input())
shousuo = [0 for i in range(time)]
shuzhang = [0 for i in range(time)]
for i in range(time):
    nums = input().split()
    shousuo[i] = int(nums[0])
    shuzhang[i] = int(nums[1])
n = 0
time_n = []
i = 0
while True:
    if 90 <= shousuo[i] <= 140 and 60 <= shuzhang[i] <= 90:
        n += 1 
        i += 1
        if i == time:
            time_n.append(n)
            break
    else:
        time_n.append(n)
        n = 0
        i += 1
        if i == time:
            break
print(max(time_n))