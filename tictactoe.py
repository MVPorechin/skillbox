class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    def __init__(self, status=None, num_cell=None):
        self.status = status
        self.num_cell = num_cell

    def __str__(self):
        return f'{self.status}\t'


class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        self.board = [[Cell('*', ord_y) for ord_y in range(3)] for ord_x in range(3)]

    def print_board(self):
        for ord_y in self.board:
            print(*ord_y)
            # print(' '.join(map(str, ord_y)))
            # print(*cell, sep='')

    def change_value_cell(self, user, ord_y, ord_x):
        self.board[ord_y][ord_x] = user


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    player_win = False
    wall_of_fame = dict()

    # класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    def __init__(self, condition_game, players_list, field):
        self.condition_game = condition_game
        self.players_list = players_list
        self.field = field

    # Метод запуска одного хода игры.
    # Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок.
    # Если игрок победил, возвращает True, иначе False.

    def one_step(self, player):
        player_ord_y, player_ord_x = [int(value) for value in input(f'{player.name} делает ход: ').split()]
        self.field.change_value_cell(player.symbol, player_ord_y, player_ord_x)
        self.field.print_board()
        for line in self.rows() + self.columns() + self.diagonals():
            sym = set(line)
            if player.symbol in sym and len(sym) == 1:
                return True
        else:
            False

    def rows(self):
        return self.field.board[:]

    def columns(self):
        return [[row[index] for row in self.field.board] for index in range(3)]

    def diagonals(self):
        backslash = [self.field.board[index][index] for index in range(3)]
        slash = [self.field.board[index][len(self.field.board[index]) - index - 1] for index in range(3)]
        return [backslash, slash]

    def cleanboard(self):
        return [[self.field.change_value_cell('*', ord_y, ord_x) for ord_y in range(3)] for ord_x in range(3)]

    def currient_session(self):
        self.field.print_board()
        while not self.condition_game:
            for player in self.players_list:
                if self.one_step(player):
                    print(f'{player.name} победил!')
                    Game.wall_of_fame[player.name] = 1
                    self.cleanboard()
                    self.print_wall_of_fame()
                    return True
                    # Метод запуска одной игры.
        # Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или ничьей.
        # Если игра завершена, метод возвращает True, иначе False.
        pass

    def print_wall_of_fame(self):
        return [print(f'Игрок {key}, счет: {self.wall_of_fame[key]}') for key in
                sorted(self.wall_of_fame, key=self.wall_of_fame.get, reverse=True)]

    def run_game(self):
        self.currient_session()
        while True:
            ask_a_question = input('Игра завершена, запустить заново? "Да" или "Нет": ').lower()
            if ask_a_question == 'да':
                self.currient_session()
                print('Доска победы')
                # self.print_wall_of_fame()
                return True
            else:
                break

    # Основной метод запуска игр.
    # В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть.
    # После каждой игры выводится текущий счёт игроков.
