violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

score_time = 0
num_select_song = int(input('Сколько песен выбрать? '))
for _ in range(1, num_select_song + 1):
    name_song = input(f'Введите {_} песню: ')
    if name_song in violator_songs:
        score_time += violator_songs[name_song]

print(f'\nОбщее время звучания песен: {round(score_time, 2)} минуты')

# зачет!
