import time


class Timer:
    def __init__(self) -> None:
        print('Время работы кода')
        self.start = None

    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(time.time() - self.start)
        # if exc_type is TypeError:
        #     return True
        return True


with Timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 1000000
    val_1 += 'abc'
with Timer() as t2:
    print('Вторая часть')
    val_3 = 200 * 200 ** 1000000

with Timer() as t3:
    print('Третья часть')
    val_3 = 200 * 200 ** 1000000
