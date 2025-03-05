n = int(input())
sum = 0
if n == 0:
    print(0)
else:
    for i in range(n):
        sum += int(input())
    print('%d %.5f' % (sum , sum / n))
