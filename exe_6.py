products = []

number = 1

com_stop = ""

while com_stop != 'stop':
    name = input("Наименование товарa: ")
    price = input("Цена товара: ")
    amount = input("Количество товара: ")
    units = input("Единицы: ")
    products.append(
        (number, {'name', name, 'price', price, 'amount', amount, 'unis', units})
    )
    number += 1
    com_stop = input("Введите 'stop' для окончания ввода: ")

print(products)

result_dict = {}

for numb, prod_dict in products:
    for key, value in prod_dict.items():
        if not result_dict.get(key):
            result_dict[key] = [value]
        else:
            result_dict[key].append(value)

for key, value in result_dict.items():
    result_dict[key] = list(set(value))

print(result_dict)
