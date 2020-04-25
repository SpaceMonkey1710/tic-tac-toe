from models import Player, Board

class Game:
    figures = ('X', 'O')
    current_player_index = 0

    def __init__(self):
        self.players = self.create_players()
        self.board = Board(width=3, height=3)

    def create_players(self):
        players_list = []
        for figure in self.figures:
            player = Player(f'Введите имя игрока, который ходит {figure}:', figure)
            players_list.append(player)
        return players_list

    def get_coords(self, position):
        position = int(position)
        row_number = (position - 1) // self.board.row_count
        cell_number = (position - 1) % self.board.row_length
        return row_number, cell_number

    def check_move(self, position):
        valid_options = [str(x) for x in range(1, self.board.cell_count + 1)]
        if position not in valid_options:
            print(f'Ошибка! Введите число от 1 до {self.board.cell_count}')
            return False

        position = int(position)
        row_number, cell_number = self.get_coords(position)
        if self.board.state[row_number][cell_number]:
            print(f'Ошибка! Ячейка {position} уже занята!')
            return False

        return True

    def check_win(self):
        current_player = self.players[self.current_player_index]
        win_status = False
        check_sets = []

        for row in self.board.state:
            check_sets.append(row)

        for column_number in range(self.board.row_length):
            column = [row[column_number] for row in self.board.state]
            check_sets.append(column)

        right_diagonal = [self.board.state[x][x] for x in range(self.board.row_length)]
        left_diagonal = [self.board.state[-x][x-1] for x in range(1, self.board.row_length + 1)]
        check_sets.extend([right_diagonal, left_diagonal])

        for combination in check_sets:
            match_elements = [cell for cell in combination if cell == current_player.figure]
            if len(match_elements) == self.board.row_length:
                win_status = True
                break

        return win_status

    def set_move(self, player, position):
        row_number, cell_number = self.get_coords(position)
        self.board.state[row_number][cell_number] = player.figure

    def turn(self):
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0

    def check_empty_cells(self):
        for row in self.board.state:
            for cell in row:
                if not cell:
                    return True
        return False

    def run(self):
        while True:
            self.board.render()
            current_player = self.players[self.current_player_index]
            position = current_player.get_position()
            move_is_valid = self.check_move(position)
            if not move_is_valid:
                continue

            self.set_move(current_player, position)

            player_wins = self.check_win()

            if player_wins:
                self.board.render()
                print(f'Победил {current_player.name}!')
                break

            if not self.check_empty_cells():
                self.board.render()
                print(f'Ходы закончились! Ничья!!!')
                break

            self.turn()