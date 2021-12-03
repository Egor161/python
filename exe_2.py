inp_list = input("Введите список: ")

entered_data = inp_list.split()
# print(entered_data)

len_list = len(entered_data)
# print(len_list)
n = 0
if len_list > 1:
    while n < len_list - 1:
       entered_data[n], entered_data [n + 1] = entered_data [n + 1], entered_data [n]

       n += 2


print(entered_data)

