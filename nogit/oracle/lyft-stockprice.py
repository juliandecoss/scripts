from operator import indexOf


prices = [3,2,6,5,0,3]
#prices = [7,1,5,3,6,4]
solution = {"profit":0,"index":[0,0]}
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        profit = prices[j]-prices[i]
        if profit > solution['profit']:
            solution['profit'] = profit
            solution["index"] = [i,j]
print(solution)