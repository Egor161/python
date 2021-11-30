seconds = int(input('Введите время в секундах: '))

constant = 60

minutes = seconds // constant
# minutes = seconds % constant

hours = minutes // constant
# hours = minutes % constant



print(hours, ":", minutes, ":", seconds)



