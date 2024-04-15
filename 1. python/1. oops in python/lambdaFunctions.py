def cube(x):
    return x*x*x
print(cube(3)) # using traditional function

cubeL = lambda x: x*x*x
print(cubeL(2)) # using lambda function

def foo(fx, x):
    return 2 + fx(x)
print(foo(cubeL,2)) # passing lambda function as argument to another function