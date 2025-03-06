n = int(input())
patients = []
# 读取病人信息
for i in range(n):
    id, age = input().split()
    age = int(age)
    patients.append((id, age, i))

# 分离老年人和非老年人
seniors = []
non_seniors = []
for patient in patients:
    if patient[1] >= 60:
        seniors.append(patient)
    else:
        non_seniors.append(patient)

# 老年人按年龄从大到小排序，年龄相同按登记先后顺序
seniors.sort(key=lambda x: (-x[1], x[2]))

# 合并排序结果
sorted_patients = seniors + non_seniors

# 输出结果
for patient in sorted_patients:
    print(patient[0])
