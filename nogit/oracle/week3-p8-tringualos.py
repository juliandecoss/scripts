s = [1, 1, 1, 3, 3]
s = [1 ,2, 3]
s = [3 ,9 ,2 ,15 ,3]
triangules = {}
counter = 0

for i in range(len(s)-2):
    temp_list = s[i:i+3]
    a = temp_list[0]
    b = temp_list[1]
    c = temp_list[2]
    ct = ((a+b-c)*(b+c-a)*(c+a-b))/(a*b*c)
    if ct>0:
        triangules[counter] = temp_list
        counter += 1
chido = triangules[max(triangules.keys())] if triangules else [-1]
print(chido)


