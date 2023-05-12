import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(1, 20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(1, 20)]
winner_team = [first_team[index] if first_team[index] > second_team[index] else second_team[index] for index in range(len(first_team))]

print(f'Первая команда: {first_team}\nВторая команда: {second_team}\nПобедители тура: {winner_team}')

# зачет!
