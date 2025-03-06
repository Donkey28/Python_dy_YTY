
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    students.append((name, score))

# 按照成绩从高到低排序，如果成绩相同则按名字字典序排序
students.sort(key=lambda x: (-x[1], x[0]))

for name, score in students:
    print(name, score)
