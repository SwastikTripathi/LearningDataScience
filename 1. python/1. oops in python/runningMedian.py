from functools import reduce
n = list(map(int, input().split()))
sum = lambda x,y: x+y
i = 1
for j in n:
    newl = n[0:i]
    newSum = reduce(sum,newl)
    median = newSum/i
    print(median)
    i=i+1