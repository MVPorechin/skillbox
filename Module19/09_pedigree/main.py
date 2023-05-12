ancestral_tree = dict()
first_parient = True
generation = 0
depth_ancestral_tree = int(input('Введите количество человек: '))
for pair in range(1, depth_ancestral_tree):
    text = input(f'{pair} пара: ').split()
    list_text = list(text)

    if first_parient:
        ancestral_tree[list_text[1]] = generation
        generation = 1
        ancestral_tree[list_text[0]] = generation
        first_parient = False

    elif generation > 0:
        for key, value in list(ancestral_tree.items()):
            if list_text[1] in key:
                ancestral_tree[list_text[0]] = value + 1

for key in sorted(ancestral_tree):
    print(key, ancestral_tree[key])

# зачет!
