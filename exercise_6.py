a = int(input("Введи количество километров: "))
b = int(input("Введи цель: "))

days = 1

print(days, "День", a)

while b > a:
    a = a + a/100*10
    days += 1
    print(days, "День", a)

print("Ответ: на", days, "день спортсмен достиг результата", b, "км.")
