# 查找第一个仅出现一次的字符
s = input()
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char in s:
    if char_count[char] == 1:
        print(char)
        break
else:
    print("no")
