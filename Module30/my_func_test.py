def func() -> None:
    print('Я функция func из my_func_test и вывожу это на экран')


if __name__ == '__main__':
    print('принт 2')
    func()
else:
    print(f'импортирован модуль {__name__}')