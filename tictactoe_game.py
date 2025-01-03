from tictactoe import HumanPlayer, RandomComputerPlayer
from tictactoe import GeniusComputerPlayer
import time

class tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # creates a 3x3 board
        self.current_winner = None  # tracks the winner

    def print_board(self):  # display current state of the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():  # display the possible moves
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):  # return the squares that are still empty
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):  # check if empty squares are left
        return ' ' in self.board

    def num_empty_squares(self):  # count and return the no. of empty squares
        return self.board.count(' ')

    def make_move(self, square, letter):  # make move
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):  # make if this move wins the game
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):  # check if the user with letter given won the game
        row_ind = square // 3  # check the row of the move
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3  # check the column of the move
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:  # check the diagonal (0,2,4,6,8)
            diagonal1 = [self.board[i] for i in [0,4,8]]  # check the main diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]  # check the anti diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        return False  # if no win return false

def play(game, x_player, o_player, print_game=True):  # main function
    if print_game:
        game.print_board_nums()  # print the board
    letter = 'X'  # start with letter 'X'
    while game.empty_squares():
        if letter == 'O':  # determine which player turn it is
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):  # attempt to make a move
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:  # check if there is a winner
                if print_game:
                    print(letter + ' wins ')
                return letter  # end the game with the winner

            letter = 'O' if letter == 'X' else 'X'  # switch players

        if print_game:
            time.sleep(0.8)

    if print_game:
        print('It\'s a tie')


if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(100):
        x_player = GeniusComputerPlayer('X')  # human player for 'X'
        o_player = RandomComputerPlayer('O')  # computer player for 'O'
        t = tictactoe()
        result = play(t, x_player, o_player, print_game=False)  # start the game
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'after 100 iterations, we see {x_wins} "X" wins, {o_wins} "O" wins and {ties} ties')