import re


#re
text = 'AV text AV'
res = re.match(r'AV', text)
print(f'поиск в начале строки по шаблону: {res}')
print(res.group())
print(res.start())
print(res.end())

print('_' * 40)

result = re.search(r'text', text)
print(result)

print('_' * 40)

result_ = re.findall(r'AV', text)
print(result_)

print('_' * 40)

text_ = 'AV text AV india is Indisa india AV'

result__ = re.sub(r'india', 'Goa', text_)
print(result__)

print('_' * 40)

pattern = re.compile('AV')
result2 = pattern.findall(text_)
print(result2)

result3 = pattern.findall(text)
print(result3)