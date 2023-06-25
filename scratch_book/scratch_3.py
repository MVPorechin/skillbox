class Example_1:
    def __add__(self, other):
        return Example_2()


class Example_2:
    answer = 'сложили два класса и вывели'


a = Example_1()
b = Example_2()
c = a + b
print(c.answer)
