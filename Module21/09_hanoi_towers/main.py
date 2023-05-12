def move(n, x, y, temp):
    if n == 1:
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
        return
    move(n - 1, x, temp, y)
    print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
    move(n - 1, temp, y, x)


count_disk = int(input('Введите количество дисков: '))
move(count_disk, 1, 3, 2)

# зачет!
