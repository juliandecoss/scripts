s = "ababbb"
size = len(s)
a = s[:size//2]
b = list(s[size//2:])
change = 0
for str in a:
    if str in list(b):
        ind = b.index(str)
        b.pop(ind)
    else:
        change += 1
print(change)