nums = input().split()
a = float(nums[1])
b = float(nums[2])
c = float(nums[3])
d = float(nums[4])
x = float(nums[0])

fx = a * x ** 3 + b * x ** 2 + c * x + d
print('%.7f'% fx)