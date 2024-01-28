#@https://habr.com/ru/companies/otus/articles/725374/


def yell(text: str) -> str:
    return text.upper() + '!'


yell('hello')

bark = yell
bark('woof')