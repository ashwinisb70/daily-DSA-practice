def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90,
           50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC",
               "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""

    for i in range(len(val)):
        while num >= val[i]:
            result += symbols[i]
            num -= val[i]

    return result

num = int(input("Enter integer: "))

print("Roman:", int_to_roman(num))
