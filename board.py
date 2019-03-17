from random import choice, choices
from logging import warning


class Board:
    BOMB, SPACE, EMPTY = 'B', 'S', 'X'

    def __init__(self, length=None, width=None, bomb_range=None):
        self.board = None
        self.length = length
        self.width = width
        self.bomb_range = bomb_range
        if length and width and bomb_range:
            self.prepare_board()
        else:
            warning('Board is not set up because length or width or'
                    'bomb range were empty.')

    def new_board(self):
        return [[self.SPACE for _ in range(self.length)]
                for _ in range(self.width)]

    def empty_board(self):
        return [[self.EMPTY for _ in range(self.length)]
                for _ in range(self.width)]

    def set_board(self, length, width, bomb_range):
        self.length = length
        self.width = width
        self.bomb_range = bomb_range

    def set_bombs(self):
        for i in range(self.width):
            bomb_positions = None
            indexes = range(self.length)
            amount = choice(self.bomb_range)
            bomb_positions = choices(indexes, k=amount)
            for position in bomb_positions:
                self.board[i][position] = self.BOMB
                self.bomb_count += 1

    def set_surrounding_bomb_points(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(self.width):
            for j in range(self.length):
                if self.board[i][j] == 'S':
                    points = 0
                    for x, y in directions:
                        if self.bomb_sorrounding(i + x, j + y):
                            points += 1
                    if points != 0:
                        self.board[i][j] = str(points)

    def bomb_sorrounding(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.length or \
          self.board[x][y] != 'B':
            return False
        return True

    def prepare_board(self):
        self.bomb_count = 0
        self.board = self.new_board()
        self.set_bombs()
        self.set_surrounding_bomb_points()

    def get_locations(self):
        locations = set()
        bomb_locations = set()
        for i in range(self.width):
            for j in range(self.length):
                if self.board[i][j] != self.BOMB:
                    locations.add((i, j))
                else:
                    bomb_locations.add((i, j))
        return locations, bomb_locations

    def get_bomb_count(self):
        return self.bomb_count

    def reset(self):
        self.board = self.new_board()
        self.prepare_board()

    def print_board(self, board):
        strings = []
        for row in board:
            strings.append(' '.join(row))
        print('\n'.join(strings))
    
    def stats(self):
        _min, _max = self.bomb_range[0], self.bomb_range[-1]
        print(f'Board is {self.length}x{self.width}.\n'
              f'There are about {_min} to {_max} bombs per row.\n')

    def __str__(self):
        strings = []
        for row in self.board:
            strings.append(' '.join(row))
        return '\n'.join(strings)
