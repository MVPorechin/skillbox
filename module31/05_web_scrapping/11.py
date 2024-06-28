import re, requests

# В данном случае запрос request.get заменен на загрзку сайта из файла html

with open('examples.html', 'r') as f:
    text = f.read()
    pattern = '<h3>(.+)</h3>'
    result = re.findall(pattern, text)


# По итогу вы так же получаете код сайта в виде одной строки

def scraptitles(url: str) -> list:
    '''Функция сохраняет HTML страницу по заданному URL
    и возвращает список строк совпавших с паттерном'''
    page = requests.get(url)
    with open('page.html', 'wb') as file:
        file.writelines(page)

    with open('page.html', 'r') as file:
        text = file.read()
        pattern = '<h3>(.+)</h3>'
        result = re.findall(pattern, text)
    return result


def main():
    print('Первая часть задания: ')
    print(result)
    print('Вторая часть: ')
    url: str = 'https://www.columbia.edu/~fdc/sample.html'
    try:
        print(scraptitles(url))
    except:
        print('Что-то сломалось.')


if __name__ == '__main__':
    main()
