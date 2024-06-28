class MyDict:
    """
    Класс MyDict описывающий словарь
    __my_dict(dict) = инициирование словаря для экземпляра
    Args:
        :param key: Ключ
        :param value: значение
    """
    __my_dict = {}

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.__my_dict[self.key] = self.value

    def __str__(self):
        """
        Метод возвращает словарь в виде строки
        :return: возвращает словарь
        """
        return f'{self.__my_dict}'

    def add(self, add_key, add_value):
        """
        Метод обновляет значение add_value в словарь,
        иначе добавляет в словарь объект ключ:значение.
        :param add_key: Ключ
        :param add_value: значение
        """
        if add_key in self.__my_dict:
            self.__my_dict[add_key] = add_value
        else:
            self.__my_dict[add_key] = add_value

    def get(self, keyname=0, default_value=0):
        """
        Метод возвращает значение элемента с указанным ключом
        :param keyname: ключ словаря
        :param default_value: значение по умолчанию
        :return: возвращает значение элемента. Если ключа нет возвращает default_value=0
        """
        if keyname in self.__my_dict:
            return self.__my_dict[keyname]
        for key, value in self.__my_dict.items():
            if isinstance(value, dict):
                return self.get(value, keyname)
            else:
                return default_value
