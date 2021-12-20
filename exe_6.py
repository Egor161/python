from itertools import cycle, count

n = 11
my_list = [x for x in range(4)]
counter = count()
cycle = cycle(my_list)

print([next(cycle) for x in range(n)])
print([next(counter) for x in range(n)])




