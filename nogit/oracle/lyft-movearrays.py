
from operator import indexOf


nums = [0,1,0,3,12]
counter = 0
while 1:
    try:
        i = nums.index(0)
        nums.pop(i)
        counter += 1
    except:
        for j in range(counter): nums.append(0)
        break
nums = nums+ [0,0]
print(nums)