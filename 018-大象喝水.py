s = input()
nums = s.split()
h = int(nums[0])
r = int(nums[1])
Pi = 3.14159
V = Pi * r * r * h
remain = 20 * 10 ** 3 % V
full = int(20 * 10 ** 3 // V)
if remain == 0:
    print(full)
else:
    print(full + 1)