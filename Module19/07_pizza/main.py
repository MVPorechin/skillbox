def order_pizza():
    count_of_order = int(input('Введите количество заказов: '))
    dict_order = dict()
    for number_order in range(1, count_of_order + 1):
        check_pizza = False
        check_client = False
        input_string_order = input(f'{number_order} заказ: ').split()
        list_order = list(input_string_order)
        for key in dict_order.keys():
            if key == list_order[0]:
                check_client = True
        if check_client:
            for key_p in dict_order[list_order[0]].keys():
                if list_order[1] == key_p:
                    check_pizza = True
            if check_pizza:
                for key_pizza, value_pizza in dict_order[list_order[0]].items():
                    if key_pizza == list_order[1]:
                        dict_order[list_order[0]][list_order[1]] = value_pizza + int(list_order[2])
            else:
                dict_order[list_order[0]][list_order[1]] = int(list_order[2])
        else:
            dict_order[list_order[0]] = {list_order[1]: int(list_order[2])}
    return dict_order


def print_client(client_order_dict):
    for key, value in client_order_dict.items():
        print(f'{key}: ')
        for key_value, v_value in value.items():
            print(f'\t{key_value}: {v_value}')


output = print_client(order_pizza())

# зачет!
