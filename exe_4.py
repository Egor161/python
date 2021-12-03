words = input("Введите фразу: ").split()

for num, word in enumerate(words):

    print(f'{num+1} - {word[:10]}')
