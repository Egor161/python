def generator (number):
    var = 1
    for x in range(1, number + 1):
        var *= x
        yield var

n = 4
for ind, el in enumerate(generator(n)):
    print(f"#{ind + 1} {el}")






