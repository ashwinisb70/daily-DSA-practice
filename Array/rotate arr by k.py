arr = [1, 2, 3, 4, 5, 6, 7]
k=3
k = k%len(arr)
result=arr[-k:]+arr[:-k]
print(result)
