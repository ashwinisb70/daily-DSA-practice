arr = [3, 5, 1, 8, 2]

minimum = arr[0]
maximum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Smallest element:", minimum)
print("Largest element:", maximum)
