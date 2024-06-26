import requests
import json
# import swapi

# Задача 1. Звёздные войны
# Повторите пример парсинга, разобранный в видео: перейдите на сайт с API, посвящённый вселенной Star Wars.
# После этого сгенерируйте реквест-ссылку на данные о человеке под номером 3 (people/3/).
# Затем напишите программу, которая парсит данные об этом человеке,
# изменяет его имя на ваше собственное и сохраняет результат в виде JSON-файла.
#
# Дополнительно: обратите внимание на значение ключа homeworld — там также хранится ссылка.
# В том же коде спарсите эту ссылку и посмотрите, что там.
# Примечание: API тоже пишут люди, а значит, время от времени его могут как-то менять и усовершенствовать,
# поэтому будьте внимательны: может быть, ссылка уже хранится в другом ключе.


result = requests.get("https://swapi.dev/api/people/3/")
if result.status_code == 200:
    json_dict = json.loads(result.text)
    json_dict['name'] = input("Введите имя: ")
    with open("swap.json", "w") as file:
        json_text = json.dump(json_dict, file, indent=4)

    # Доп:
    result_homeworld = requests.get(json_dict['homeworld'])
    print(result_homeworld.text)


# Задача 2. Документация API
# Обычно к открытым API прилагается подробная документация,
# где описывается логика формирования ссылок и какие данные по ним можно получать (или отправлять!).
#
# Изучите документацию того же сайта по «Звёздным войнам».
#
# Поэкспериментируйте с получением данных о кораблях, планетах, фильмах и так далее.
# А ещё попробуйте библиотеку swapi (о ней также в документации)
# и с её помощью выведите начало сюжета из фильма «Новая надежда» (A New Hope).


# print(swapi.get_film(1))
# Сейчас библиотека не работает, получить начало сюжета можно напрямую

result = requests.get("https://swapi.dev/api/films/1/")

json_dict = json.loads(result.text)

print('\n', json_dict["opening_crawl"])
