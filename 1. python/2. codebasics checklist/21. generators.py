def square(x):
    yield x**2

n = int(input())
arr = [square(i) for i in range(n)]
# arr = [i**2 for i in range(1,n+1)]
print(arr)