arr = [1, 2, 3, 7, 5]
target = 12
for i in range (len(arr)):
    total = 0
    for j in range(i,len(arr)):
        total += arr[j]
        if total == target:
            print("subarray found from", i, "to", j)
