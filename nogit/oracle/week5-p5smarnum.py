def is_smart_number(num):
    factors = 0
    for n in range(1,num+1):
        if num % n == 0:
            #print(n)
            factors += 1
    if factors % 2 == 0:
        print("NO")
    else:
        print("YES")
ar = [1,2,7,169]

for a in ar:
    is_smart_number(a)
