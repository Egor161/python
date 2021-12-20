list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [list[x] for x in range(1, len(list)) if list[x] > list[x - 1]]
print(result)




