from typing import List, Tuple, Any


letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

my_zip: List[Tuple[Any, Any]] = list(map(lambda let, num: (let, num), letters, numbers))
print(my_zip)

# зачет!
