def lagrange(n, level):
    if level == 0:
        return 0
    sqrtn = int(n ** 0.5)
    if sqrtn * sqrtn == n:
        return str(sqrtn)
    while sqrtn > 0:
        if lagrange(n - sqrtn * sqrtn, level - 1) != 0:
            return str(sqrtn) + " " + lagrange(n - sqrtn * sqrtn, level - 1)
        sqrtn -= 1
    return 0


n = int(input('Введите число: '))
print(lagrange(n, 4))

# count_members = int(input(''))
# if count_members % 2 == 0:
#     print()
