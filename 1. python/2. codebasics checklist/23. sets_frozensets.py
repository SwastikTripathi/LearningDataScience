set1 = {1,2,3,4,5}
set2 = frozenset(set1)
set1.add(6)
try:
    set2.add(6)
except AttributeError:
    print('frozenset is immutable')
print(set1)
print(set2)

set3 = {1,2,3,4,5}
set4 = {4,5,6,7,8}
set5 = set()
for i in set3:
    if i not in set4:
        set5.add(i)
print(set5)