import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # If it's the first move, choose the center or a random corner
        if len(game.available_moves()) == 9:
            # Prefer center if available
            if 4 in game.available_moves():  # Assuming center is index 4
                return 4
            else:
                return random.choice([0, 2, 6, 8])  # Random corner
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # AI's letter
        other_player = 'O' if player == 'X' else 'X'

        # Base cases
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': (1 if other_player == max_player else -1) * (state.num_empty_squares() + 1)
            }

        if not state.empty_squares():  # Tie
            return {'position': None, 'score': 0}

        # Recursive case: maximize for AI, minimize for opponent
        best = {'position': None, 'score': -math.inf if player == max_player else math.inf}

        for move in state.available_moves():
            # Simulate the move
            state.make_move(move, player)
            sim_score = self.minimax(state, other_player)  # Recursively calculate score
            # Undo the move
            state.board[move] = ' '
            state.current_winner = None  # Reset winner after undoing the move
            sim_score['position'] = move

            # Update best score
            if player == max_player:  # Maximizing
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:  # Minimizing
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best