arr = [1,2,3,4]
result=[]
for i in range(len(arr)):
    p = 1
    for j in range(len(arr)):
        if i!=j:
            p = p*arr[j]
    result.append(p)
print(result)
