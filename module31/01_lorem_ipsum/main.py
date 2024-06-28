import re


text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

pattern_word = r"\b\w{4}\b"
if __name__ == "__main__":
    result = re.findall(pattern=pattern_word, string=text)
    print(f'Список слов, состоящих ровно из четырёх букв: {result}')