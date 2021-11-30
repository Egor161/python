cash = int(input("Введите значение выручки: "))
costs = int(input("Введите издержки: "))

if cash > costs:
    print("Все ОК")
    print("Рентабильность фирмы: ", cash//costs)
    employee = int(input("Введите количество сотрудников: "))
    print("Прибыль на одного сотрудника:", cash//employee, "руб")

else:
    print("Увеличте выручку, уменьшите затраты")

