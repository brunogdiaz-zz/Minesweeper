from board import Board

# I might be needing a State object


class Minesweeper:
    DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, difficulty='easy'):
        self.game_board = None
        self.player_board = None
        self.difficulty = difficulty
        self.width = None
        self.length = None
        self.locations = None
        self.bomb_locations = None

    def play(self):
        self.new_game()
        playing = True
        print('NEW GAME')
        print('Current Player Board')
        self.game_board.print_board(self.player_board)
        while playing:
            print()
            print('Type in your position to click(Example: 3,4)')
            print('Position:', end=' ')
            position = input()
            x, y = [int(n) - 1 for n in position.split(',')]
            output = self.handle_action(x, y, set())
            if output == -1:
                playing = False
                self.game_over()
            else:
                print()
                print('Current Player Board')
                self.game_board.print_board(self.player_board)
            # print('LOCATIONS LEFT', self.locations)
            if len(self.locations) == 0:
                print('!!!YOU WON!!!')
                playing = False

    def new_game(self):
        self.game_board = Board(self.difficulty)
        self.width = self.game_board.width
        self.length = self.game_board.length
        self.game_board.prepare_board()
        self.player_board = self.game_board.empty_board()
        self.locations, self.bomb_locations = self.game_board.get_locations()

    def handle_action(self, x, y, visited):
        if x < 0 or y < 0 or x >= self.width or y >= self.width or (x, y) in visited:
            return 0
        if self.game_board.board[x][y] == 'B':
            self.set_all_bombs_for_player()
            return -1
        if (x, y) in self.locations:
            self.locations.remove((x, y))
        if self.game_board.board[x][y] == 'S':
            self.player_board[x][y] = 'S'
            visited.add((x, y))
            for x2, y2 in self.DIRECTIONS:
                if self.handle_action(x + x2, y + y2, visited) == -1:
                    return -1
        else:
            self.player_board[x][y] = self.game_board.board[x][y]
            return 0

    def set_all_bombs_for_player(self):
        for x, y in self.bomb_locations:
            self.player_board[x][y] = 'B'

    def game_over(self):
        print('SOWY YOU LOST')
        print('YOUR GAME BOARD')
        self.game_board.print_board(self.player_board)
        print()
        print('ACTUAL GAME BOARD')
        print(self.game_board)
        print()
        print('Do you wanna play again? (Type Y/N): ', end=' ')
        play_again = input()
        if play_again == 'Y':
            self.play()
        else:
            print('Play again later!')
