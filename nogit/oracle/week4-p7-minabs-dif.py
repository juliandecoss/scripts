arr = [3, -7, 0]
response ={}
res = []
max_pos = len(arr)
arr.sort()
for pos,a in enumerate(arr):
    if pos < max_pos-1:
        diff = abs(a-arr[pos+1])
        if not res:
            res.append(diff)
        elif min(res) > diff:
            res.append(diff)
print(min(res))