class Player:
    def __init__(self, initial_text, figure):
        self.name = input(initial_text)
        self.figure = figure

    def __str__(self):
        return f'<Player: {self.name} ({self.figure})>'

    def get_position(self):
        return input(f'Ходит {self.name} ({self.figure}):').strip()


class Board:
    def __init__(self, width, height):
        self.state = [['' for _ in range(width)] for _ in range(height)]

    def render(self):
        for row in self.state:
            for i, cell in enumerate(row):
                sep = ' ' if i + 1 < len(row) else '\n'
                print(cell or '_', end=sep)

    @property
    def cell_count(self):
        return len(self.state[0]) * len(self.state)

    @property
    def row_length(self):
        return len(self.state[0])

    @property
    def row_count(self):
        return len(self.state)


