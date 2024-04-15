integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

res = dict(zip(integer, binary))
print(res)

inv = [-1*i for i in integer]
print(inv)

sq = {i**2 for i in integer}
print(sq)