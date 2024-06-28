from SquareIter import SquareIterator


my_iter = SquareIterator(number=64)

my_iter.square_by_class_iter()
for num in my_iter:
    print(num)

my_iter.function_generator()

for num in my_iter.expression_generator():
    print(num)

# зачет!

my_iter._new_var = 2
print(my_iter._new_var)
my_iter.__my_var = 3
print(my_iter.__my_var)