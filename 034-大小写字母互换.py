s = input()
out = ''
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        out += chr(ord(s[i]) + 32)
    elif 97 <= ord(s[i]) <= 122:
        out += chr(ord(s[i]) - 32)
    else:
        out += s[i]
print(out)