from functools import reduce

# MAP function
l = [1,3,5,7]
cubeL = lambda x:x*x*x
newl = list(map(cubeL, l))
# can also be written as
# newl = list(map(lambda x:x*x*x, l))
print(newl)

# FILTER function
def filterFun(x):
    return x>3
newl2 = list(filter(filterFun,l))
print(newl2)

# REDUCE function
sum = reduce(lambda x,y:x+y, l)
print(sum)
