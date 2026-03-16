arr=[4, 2, -3, 1, 6]
found = False
for i in range(len(arr)):
    total = 0
    for j in range(i,len(arr)):
        total+=arr[j]
        if total == 0:
            found == True
print("Zero Sum Subarray exists:",found)
