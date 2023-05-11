def missingNumbers(arr, brr):
    res = []
    brr_frequency = {}
    arr_frequency = {}
    for i in brr:
        if brr_frequency.get(i):
            brr_frequency[i] = brr_frequency[i] +1
        else:
            brr_frequency[i] = 1
    for i in arr:
        if arr_frequency.get(i):
            arr_frequency[i] = arr_frequency[i] +1
        else:
            arr_frequency[i] = 1
    for j in brr_frequency.keys():
        if arr_frequency.get(j):
            if arr_frequency[j] != brr_frequency[j]:
                res.append(j)
        else:
            res.append(j)
    return res.sort()

arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
a  = missingNumbers(arr,brr)
print(a)