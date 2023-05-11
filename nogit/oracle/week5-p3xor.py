n= 2
queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
col = [[] for i in range(n)]
res = []
lastanswer = 0
#breakpoint()
for qu in queries:
    data = (qu[1]^lastanswer)%n
    if qu[0] == 1:
        col[data].append(qu[2])
    elif qu[0] == 2:
        breakpoint()
        ind_x = qu[2]%len(col[data])
        lastanswer = col[data][ind_x]
        res.append(lastanswer)
print(col)
print(res)
