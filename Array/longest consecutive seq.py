arr=[100, 4, 200, 1, 3, 2]
S = set(arr)
longest = 0
for num in S:
    if num -1 not in S:
        length = 1
        while num+length in S:
            length+=1
        longest=max(longest,length)
print("longest sequence length:",longest)
