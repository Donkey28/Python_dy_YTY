n = int(input())
s0 = input()
old_num = s0.split()
old_rate = int(old_num[1]) / int(old_num[0])
rate = [0 for i in range(n-1)]
for i in range(n-1):
    s = input()
    nums = s.split()
    ok_rate = int(nums[1]) / int(nums[0])
    rate[i] = ok_rate

for i in range(n-1):
    if rate[i] - old_rate > 0.05:
        print("better")
    elif rate[i] - old_rate < -0.05:
        print("worse")
    else:
        print("same")