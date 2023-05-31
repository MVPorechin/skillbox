from Elements import Water
from Elements import Wind
from Elements import Fire
from Elements import Earth
from Elements import Snow
from Elements import Ice
from Elements import Gas

class_element = [Wind(), Water(), Fire(), Earth(), Snow(), Ice(), Gas()]
list_elem = [elem for elem in class_element]

mixed_elem = [print(first_elem + second_elem) for first_elem in list_elem for second_elem in list_elem]
