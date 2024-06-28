import json
from typing import Any


def recursive_search_and_get_value(json_file: Any, find_item: Any):
    if isinstance(json_file, dict):
        for key, value in json_file.items():
            if key == find_item:
                yield value
            elif isinstance(value, (dict, list)):
                yield from recursive_search_and_get_value(value, find_item)
    elif isinstance(json_file, list):
        for item in json_file:
            yield from recursive_search_and_get_value(item, find_item)


def comparsion_json(first_json: str, second_json: str, list_of_differences: list) -> dict[Any, Any]:
    result = {}

    with (
        open(file=first_json, mode='r') as file_json_new,
        open(file=second_json, mode='r') as file_json_old
    ):
        old_data = json.load(file_json_old)
        new_data = json.load(file_json_new)

    for elem in diff_list:
        result_diff_new_json = recursive_search_and_get_value(json_file=new_data, find_item=elem)
        result_diff_old_json = recursive_search_and_get_value(json_file=old_data, find_item=elem)

        if result_diff_new_json != result_diff_old_json:
            for _ in result_diff_new_json:
                result[elem] = _

    return result


if __name__ == "__main__":
    json_new = 'json_new.json'
    json_old = 'json_old.json'
    diff_list = ["services", "staff", "datetime"]
    my_result = comparsion_json(
        first_json=json_new, second_json=json_old, list_of_differences=diff_list
    )
    print(my_result)
    with open(file='result.json', mode='w') as file_result:
        json.dump(my_result, file_result, ensure_ascii=False, indent=4)
