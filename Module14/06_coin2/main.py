def detector(x_coordinate, y_coordinate, radius):
    if x_coordinate ** 2 + y_coordinate ** 2 <= radius ** 2:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')

print('Введите координаты монетки:')
x_coordinate = float(input('X: '))
y_coordinate = float(input('Y: '))
radius = int(input('Введите радиус: '))
detector(x_coordinate, y_coordinate, radius)

# зачет!
