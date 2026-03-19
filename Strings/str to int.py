s = input("Enter string: ")

s = s.strip()
num = ""

for ch in s:
    if ch.isdigit():
        num += ch
    else:
        break

if num == "":
    print(0)
else:
    print(int(num))
