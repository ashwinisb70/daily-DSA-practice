arr=[0,1,0,3,12]
for i in range(len(arr)):
    if arr[i]==0:
        arr.append(arr.pop(i))
print("array after moving zeros:",arr)
