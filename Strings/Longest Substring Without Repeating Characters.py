s = "abcabcbb"

max_len = 0
current = ""

for ch in s:
    if ch not in current:
        current += ch
        max_len = max(max_len, len(current))
    else:
        current = current[current.index(ch)+1:] + ch

print("Length:", max_len)
