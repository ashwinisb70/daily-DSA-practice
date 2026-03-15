arr=[1,2,3,4,5]
last=arr[-1]
arr=[last]+arr[:-1]
print("rotated array:",arr)
