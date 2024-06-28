class File:
    """
    Контекст менеджер
    при попытке открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи;
    на выходе из менеджера подавляются все исключения, связанные с файлами
    """

    def __init__(self, filename: str, mode: str) -> None:
        self._filename = filename
        self._mode = mode
        self._file = None

    def __enter__(self) -> None:
        try:
            self._file = open(filename=self._filename, mode=self._mode, encoding='utf-8')
        except IOError:
            self._file = open(filename=self._filename, mode="w", encoding='utf-8')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is IOError:
            self._file.close()
            return True
        else:
            self._file.close()


if __name__ == '__main__':
    with File(filename='my_test.txt', mode='w') as my_test:
        my_test.write('test01')

# зачет!
