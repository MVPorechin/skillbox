text = input('Введите строку: ')
text_dict = {}
count = 0
for letter in text:
    text_dict[letter] = text_dict.get(letter, 0) + 1

for value in text_dict.values():
    if value % 2 != 0:
        count += 1

if count <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')

# зачет!
