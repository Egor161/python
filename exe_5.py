user_rating = int(input("Введите рейтинг: "))

rating = [9, 8, 7, 6, 5, 4, 3]

inset = False
for index, elem in enumerate(rating):
    if user_rating > elem:
        rating.insert(index, user_rating)
        inset = True
        break

if not inset:
    rating.append(user_rating)

print(rating)



