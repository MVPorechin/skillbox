import random
count = int(input('Количество чисел в списке: '))
nums = [random.randint(0, 2) for _ in range(count)]
print(f'Список до сжатия: {nums}')
finish_list = [num for num in nums if num != 0]
print(f'Список после сжатия: {finish_list}')

# зачет!
