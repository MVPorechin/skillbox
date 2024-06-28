import re

from bs4 import BeautifulSoup
import requests

url = 'https://www.columbia.edu/~fdc/sample.html'

my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/111.0.0.0 Safari/537.36'}


with open(file='response.txt', mode='w') as file:
    get_page = requests.get(url=url, headers=my_headers).text
    soup = BeautifulSoup(get_page, 'html.parser')
    file.write(soup.prettify())


def web_scrapping(input_file: str):
    with open(file=input_file, mode='r') as open_file:
        soup = BeautifulSoup(open_file.read(), 'html.parser').find_all('h3')

    return [elem.text for elem in soup]


if __name__ == "__main__":

    # В данном случае запрос request.get заменен н на загрзку сайта из файла html
    example_file = web_scrapping(input_file='examples.html')
    print(example_file)
    example_url = web_scrapping(input_file='response.txt')
    print(example_url)
# По итогу вы так же получаете код сайта в виде одной строки
