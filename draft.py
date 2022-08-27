print('14.3 Командная строка и интерпретатор')
print('Задача 1. Таблица умножения: возвращение')

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end='\t')
    print()

print('Задача 2. Калькулятор')

while True:
    command = input("Выберите операцию: ")
    if command in "+-*/":
        break
    print("Ошибка: такой операции не существует. Попробуйте ещё раз.")

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))

result = 0
if command == "+":
    result = first + second
elif command == "-":
    result = first - second
elif command == "*":
    result = first * second
elif command == "/":
    result = first / second

print(f"{first} {command} {second} = {result}")

print('Задача 3. Калькулятор 2')

while True:
    command = input("Выберите операцию: ")
    if command in "+-*/":
        break
    print("Ошибка: такой операции не существует. Попробуйте ещё раз.")

count = 1
number = int(input(f"Введите число {count}: "))
result_str = str(number)
result = number
while number != 0:
    count += 1
    number = int(input(f"Введите число {count}: "))

    if command == "+":
        result += number
    elif command == "-":
        result -= number
    elif command == "*":
        result *= number
    elif command == "/":
        result /= number
    result_str += " " + command + " " + str(number)

print(result_str + " = " + str(result))

print('14.4 Работа в PyCharm. Отладка программ')
print('Задача 2. НОД')
def gcd(a, b):

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    print('Наибольший общий делитель:', a + b)

gcd(30, 18)