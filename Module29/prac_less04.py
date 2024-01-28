# Задача 1. Createtime
#
# Реализуйте декоратор класса, который выдаёт дату и время создания, а также список всех методов объекта класса
# каждый раз, когда объект класса создаётся в основном коде.
#
#
#
import datetime


def decorator(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)

        print("Время создания -", datetime.datetime.now())
        print("Методы:", end=" ")
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            print(i_method, end=' ')
        print()
        return instance

    return wrapper


@decorator
class Example:

    def hello(self):
        print("hello")

    def hello_2(self):
        print("hello")


Example()
Example()


# Задача 2. Декорацию знаешь?
#
# На новой работе вы познакомились с middle-разработчиком на Python, который согласился научить вас всему,
# что умеет сам. Но перед этим он решил точечно проверить ваши знания. Он показал код, где один и тот же декоратор
# логирования использовался для каждого метода класса отдельно: Зная, что классы тоже можно декорировать,
# вы сразу поняли, как можно упростить код.
#
# Реализуйте декоратор logging, который должен декорировать класс и логировать каждый метод в нём.
# Логирование реализуйте на своё усмотрение:
#
# это может быть, например, вывод названия метода, его аргов, кваргов и документации на экран;
# либо вывод всей этой информации в отдельный файл вместе с датой и временем.

print('2')
def logged(func):
    def wrapped(*args, **kwargs):
        print("Запуск функции произошёл в:", datetime.datetime.now())
        return func(*args, **kwargs)

    return wrapped


def decorator(cls):
    for i_method in dir(cls):
        if i_method.startswith('__'):
            continue
        a = getattr(cls, i_method)
        if hasattr(a, '__call__'):
            decorated_a = logged(a)
            setattr(cls, i_method, decorated_a)
    return cls


@decorator
class A:

    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


A().test_sum_1()
