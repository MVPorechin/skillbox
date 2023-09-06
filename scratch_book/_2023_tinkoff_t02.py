from typing import Dict


def create_dict_word_count(string_to_dict: str) -> Dict:
    dict_word_count = dict()
    list_string = list(string_to_dict)
    for _ in range(len(string_to_dict)):
        dict_word_count[list_string[_]] = string_to_dict.count(list_string[_])
    return dict_word_count


def coint_word_in_string(word: str, string: str) -> int:
    word_count = create_dict_word_count(string_to_dict=word)
    string_count = create_dict_word_count(string_to_dict=string)
    return min(string_count[key] // value for key, value in word_count.items())


s = input()
# s = 'fheriherffazfszkisrrs'
n = 'sheriff'
x = coint_word_in_string(word=n, string=s)
print(x)
