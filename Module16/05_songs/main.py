violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count_song = int(input('Сколько песен выбрать? '))
over_time_song = 0
for number in range(1, count_song + 1):
    name_song = input(f'Название {number}-й песни: ')
    for index in violator_songs:
        if index[0] == name_song:
            over_time_song += index[1]

print(f'Общее время звучания песен: {round(over_time_song, 2)} минуты')

# зачет!
