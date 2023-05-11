import math
x = 1534236469
is_negative = True if x < 0  else False
a = str(abs(x))
solution = "".join([a[digit]for digit in range(len(a)-1,-1,-1)])
solution =  int("-"+ solution) if is_negative else int(solution)
print(solution >= 2**31)



# print(1534236469)
# print(1534236469>=int("1"+bin,2))
# print(math.exp(32,2))