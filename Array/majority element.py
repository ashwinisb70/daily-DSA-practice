arr=[2,2,1,2,3]
for num in arr:
    if arr.count(num)>len(arr)//2:
        print("majority elements:",num)
        break
