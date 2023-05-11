arr = [7,3,100,200,300,350,400,401,402]
k = 3

arr.sort()
print(arr)
print(k)
res = {}
differences = []
for pos,n in enumerate(arr):
    if pos +k <= len(arr):
        provisional_array = arr[pos:pos+k]
        unfairness = max(provisional_array)-min(provisional_array)
        differences.append(unfairness)
        res[f"{pos}:{pos+k}"] = unfairness
        print(provisional_array)
mini =  min(differences)
print(mini)