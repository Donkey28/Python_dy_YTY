s = input()
nums = s.split()
n = int(nums[0])
x = int(nums[1])
y = int(nums[2])
full = y // x
yushu = y % x

if yushu == 0:
    print(n - full)
else:
    if n - full - 1 <= 0:
        print(0)
    else:
        print(n - full - 1)