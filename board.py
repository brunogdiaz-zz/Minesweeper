from random import choice, choices


class Board:
    BOMB, SPACE = 'B', 'S'
    EASY, MEDIUM, HARD = range(2), range(4), range(6)
    MINIMUM_SIZE = 10
    MAX_SIZE = 20

    def __init__(self, length, width, difficulty='easy'):
        if length < self.MINIMUM_SIZE:
            raise Exception(f'Length should be bigger than {self.MINIMUM_SIZE} blocks.')
        elif length > self.MAX_SIZE:
            raise Exception(f'Length should be smaller than {self.MAX_SIZE} blocks.')
        if width < self.MINIMUM_SIZE:
            raise Exception(f'Width should be bigger than {self.MINIMUM_SIZE} blocks.')
        elif width > self.MAX_SIZE:
            raise Exception(f'Width should be smaller than {self.MAX_SIZE} blocks.')

        self.length = length
        self.width = width
        self.board = None
        self.difficulty = difficulty
        self.bomb_count = 0

    def new_board(self):
        return [[self.SPACE for _ in range(self.length)] for _ in range(self.width)]

    def set_bombs(self):
        for i in range(self.width):
            bomb_positions = None
            indexes = range(self.length)
            amount = 0
            if self.difficulty == 'easy':
                amount = choice(self.EASY)
            elif self.difficulty == 'medium':
                amount = choice(self.MEDIUM)
            else:
                amount = choice(self.HARD)
            bomb_positions = choices(indexes, k=amount)
            for position in bomb_positions:
                self.board[i][position] = self.BOMB
                self.bomb_count += 1

    def set_points(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
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
        if x < 0 or y < 0 or x >= self.width or y >= self.length or self.board[x][y] != 'B':
            return False
        return True

    def prepare_board(self):
        self.bomb_count = 0
        self.board = self.new_board()
        self.set_bombs()
        self.set_points()

    def get_bomb_count(self):
        return self.bomb_count

    def reset(self):
        self.board = self.new_board()
        self.prepare_board()

    def change_difficulty(self, difficulty):
        self.difficulty = difficulty

    def __str__(self):
        strings = []
        for row in self.board:
            strings.append(' '.join(row))
        return '\n'.join(strings)
