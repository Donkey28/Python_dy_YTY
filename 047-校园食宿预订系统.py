n, m = map(int, input().split())
dishes = {}
for _ in range(m):
    name, price, quantity = input().split()
    dishes[name] = [int(price), int(quantity)]

total_income = 0
for _ in range(n):
    ordered_dishes = input().split()
    for dish in ordered_dishes:
        if dish in dishes and dishes[dish][1] > 0:
            total_income += dishes[dish][0]
            dishes[dish][1] -= 1

print(total_income)
