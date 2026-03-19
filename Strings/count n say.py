n = int(input("Enter n: "))

s = "1"

for _ in range(n - 1):
    new = ""
    count = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            new += str(count) + s[i]
            count = 1

    new += str(count) + s[-1]
    s = new

print(s)
