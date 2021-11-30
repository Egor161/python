n = int(input("Введите целое положительное число: "))

temp = n % 10

while n > 0:
    n = n//10
    if n % 10 > temp:
        temp = n % 10
print(temp)
