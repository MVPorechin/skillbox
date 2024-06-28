from Library import MyDict

mydict = MyDict(key='Maxim', value='it_specialist')
print(mydict)
mydict.add(add_key='Anna', add_value='developer')
print(mydict)
mydict.add(add_key='Anna', add_value='CEO')
print(mydict)
mydict.get('Anna')
print(mydict.get('Anna'))
print(mydict.get('Zurab'))


