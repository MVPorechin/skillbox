## Задача 3. Функция
### Что нужно сделать
Напишите функцию, которая на вход принимает кортеж и какой-то случайный элемент (его можно вводить с клавиатуры).
Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём и заканчивающийся вторым его появлением включительно.

Если элемента нет вовсе — вернуть пустой кортеж.

Если элемент встречается только один раз — вернуть кортеж, который начинается с этого элемента и идёт до конца исходного.

Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

Пример вызова функции:

```
print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
Ответ в консоли: (2, 3, 4, 5, 6, 7, 8, 2)
```
### Что оценивается
- Результат вычислений корректен.
- Весь функционал программы описан в функции(-ях)
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом — в видео 2.3).
