print('14.3 Командная строка и интерпретатор')

for i in range(1, 11):
    for j in range(1, 9):
        print(i * j, end='\t')
    print()

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

