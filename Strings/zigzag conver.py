s = input("Enter string: ")
n = int(input("Enter rows: "))

if n == 1:
    print(s)
else:
    rows = [""] * n
    i, step = 0, 1

    for ch in s:
        rows[i] += ch

        if i == 0:
            step = 1
        elif i == n - 1:
            step = -1

        i += step

    print("".join(rows))
