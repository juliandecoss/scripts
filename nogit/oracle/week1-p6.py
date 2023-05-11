def divisibleSumPairs(n, k, ar):
    # Write your code here
    counter = 0
    i = -1
    for num1 in ar:
        i += 1
        j = -1
        for num2 in ar:
            j += 1
            if i<j and (num1+num2)%k == 0:
                counter += 1
    return counter
n =100 
k = 22
ar=[43, 95, 51, 55, 40, 86, 65, 81, 51, 20, 47, 50, 65, 53, 23, 78, 75, 75, 47, 73, 25, 27, 14, 8, 26, 58, 95, 28, 3, 23, 48, 69, 26, 3, 73, 52, 34, 7, 40, 33, 56, 98, 71, 29, 70, 71, 28, 12, 18, 49, 19, 25, 2, 18, 15, 41, 51, 42, 46, 19, 98, 56, 54, 98, 72, 25, 16, 49, 34, 99, 48, 93, 64, 44, 50, 91, 44, 17, 63, 27, 3,65, 75, 19, 68, 30, 43, 37, 72, 54, 82, 92, 37, 52, 72, 62, 3, 88, 82, 71]
# n = 6
# k = 3
# ar = [1, 3, 2, 6, 1, 2]
#print(len(ar))
a = divisibleSumPairs(n,k,ar)
print(a)
diccionario = {a:pos for pos,a in enumerate(ar)}
counter = 1
max_number = max(ar)
for i,a in enumerate(ar):
    counter2 = 1
    b = 1
    #breakpoint()
    while b <= max_number:
        factor = k * counter2   
        if factor >= a:
            b= abs(a - factor)
            if diccionario.get(b) and i<diccionario.get(b):
                counter += 1
        counter2 += 1
print(counter)