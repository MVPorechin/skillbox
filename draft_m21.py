## home work
# def shortest_seq_range(string, tpl):
#     return min(len(string), len(tpl))
#
#
# syms_str = 'abcd'
# nums_tpl = (10, 20, 30, 40)
#
# pairs = ((syms_str[i_elem], nums_tpl[i_elem]) for i_elem in range(shortest_seq_range(syms_str, nums_tpl)))
# print(f'{pairs}')
def factorial(num):
    if num == 1:
        return 1
    fact_m_minus_1 = factorial(num - 1)
    return num * fact_m_minus_1


num_fuct = factorial(5)
print(num_fuct)


def fibonacci(n):
    """ Returns Fibonacci Number at nth position using recursion"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10): print(fibonacci(i), end=" ")

# Источник: https://pythononline.ru/osnovy/rekursii-python

# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой то блок',
#             'p': 'А вот тут новый абзац'
#         }
#     }
# }
#
#
# def find_key(struct, key):
#     if key in struct:
#         return struct[key]
#
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# user_key = input('Какой ключ ищем?: ')
# value = find_key(site, user_key)
# if value:
#     print(value)
# else:
#     print('Такого ключа в структуре сайта нет')