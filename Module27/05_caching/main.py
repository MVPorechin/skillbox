from my_lru_cache import my_lru_cache_decorator, timer, MyLRUCacheDecorator

# @MyLRUCacheDecorator
# @timer
@my_lru_cache_decorator
def fibonacci(number):
    """
    Функция расчета числа Фибоначчи
    :param number:
    :return:
    """
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)



# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован

# зачет!
