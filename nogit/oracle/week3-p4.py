a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
def diagonalDifference(arr):
    i = -1
    j = len(arr[0])
    fl = 0
    sl = 0
    for row in arr:
        i += 1
        j -= 1
        fl += row[i]
        sl += row[j]
    return abs(fl-sl)
a = diagonalDifference(a)
print(a)