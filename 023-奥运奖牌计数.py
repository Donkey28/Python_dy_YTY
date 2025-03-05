n = int(input())
Au = 0
Ag = 0
Cu = 0
for i in range(n):
    s = input()
    nums = s.split()
    Au += int(nums[0])
    Ag += int(nums[1])
    Cu += int(nums[2])
print("%d %d %d %d" % (Au , Ag , Cu , Au + Ag + Cu))