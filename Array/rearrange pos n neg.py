arr = [1, -2, 3, -4, -1, 4]
pos = []
neg = []
for num in arr:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)
result = []
i = 0
while i < len(pos) and i < len(neg):
    result.append(pos[i])
    result.append(neg[i])
    i +=1
print(result)
