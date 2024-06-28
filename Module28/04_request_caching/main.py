from typing import Any


class LRUCache:
    """
    Класс реализующий LRU (Least Recently Used Cache) часто повторяющиеся запросы,
    очередь ограничиваем при создании объекта
    """
    def __init__(self, capacity: int) -> object:
        self.capacity = capacity
        self._data = dict()
        self._order = list()

    def print_cache(self) -> dict:
        """
        Метод выводит на экран текущий кэш
        :return:
        """
        print('LRU Cache:')
        for key, value in self._data.items():
            print(key, ':', value)

    @property
    def get(self):
        """
        Геттер возвращает текущий весь кэш из словаря
        :return:
        """
        return self._data

    @get.setter
    def cache(self, value: tuple) -> None:
        """
        Сеттер, на входе подаем кортеж ('key', 'value').
        Проверяем сперва наличие данных в уже имеющимся кэше, в отсутствии - добавляем данные в кэш и очередь.
        :param value:
        :return:
        """
        if value[0] in self._data.keys() and value[1] == self._data[value[0]]:
            return
        if len(self._order) == self.capacity:
            self._order.pop(0)
            first_key = next(iter(self._data))
            first_value = self._data.pop(first_key)
        self._data[value[0]] = value[1]
        self._order.append(value[0])

    def get(self, key: Any) -> Any:
        """
        Метод поиска значения по ключу
        :param key: ключ
        :return: значение по ключу
        """
        if key not in self._data:
            raise KeyError(key)
        return self._data.get(key)


if __name__ == '__main__':
    # Создаем экземпляр класса LRU Cache с capacity = 3
    cache = LRUCache(3)

    # Добавляем элементы в кэш
    cache.cache = ("key1", "value1")
    cache.cache = ("key2", "value2")
    cache.cache = ("key3", "value3")

    # # Выводим текущий кэш
    cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3
    # Получаем значение по ключу
    print(cache.get("key2"))  # value2
    # Добавляем новый элемент, превышающий лимит capacity
    cache.cache = ("key4", "value4")

    # Выводим обновленный кэш
    cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4

    cache.cache = ("key5", "value5")

    # Выводим обновленный кэш
    cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4

# зачет!
