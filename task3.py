# ==================== TASKS ====================

# -------------------- Multiplication Table --------------------
def multiplication_table(n: int):
    """Prints the multiplication table for a given number."""
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def main_multiplication_table():
    print("\nMultiplication Table")
    multiplication_table(5)
    multiplication_table(3)

# -------------------- Swap Two Numbers --------------------
def swap_numbers(a: int, b: int):
    """Swaps two numbers without using a third variable."""
    return b, a

def main_swap_numbers():
    print("\nSwap Two Numbers")
    test_cases = [(5, 10), (7, 3), (0, 0)]
    for a, b in test_cases:
        print(f"Before: a={a}, b={b} | After: {swap_numbers(a, b)}")

# -------------------- Check Substring --------------------
def is_substring(s1: str, s2: str):
    """Checks if s2 is a substring of s1."""
    return s2 in s1

def main_check_substring():
    print("\nCheck Substring")
    print(is_substring("hello world", "world"))
    print(is_substring("python", "java"))

# -------------------- Decimal to Binary --------------------
def decimal_to_bin(n: int):
    """Converts a decimal number to binary."""
    return bin(n)[2:]

def main_decimal_to_bin():
    print("\nDecimal to Binary")
    print(decimal_to_bin(10))
    print(decimal_to_bin(0))

# -------------------- Matrix Addition --------------------
def matrix_add(A: list, B: list):
    """Adds two matrices element-wise."""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def main_matrix_add():
    print("\nMatrix Addition")
    print(matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print(matrix_add([[10], [20]], [[30], [40]]))

# -------------------- Matrix Multiplication --------------------
def matrix_multiply(A: list, B: list):
    """Multiplies two matrices."""
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return result

def main_matrix_multiply():
    print("\nMatrix Multiplication")
    print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print(matrix_multiply([[2, 0], [0, 2]], [[1, 3], [3, 1]]))

# -------------------- Find Second Largest --------------------
def second_largest(nums: list):
    """Finds the second largest number in a list."""
    unique_nums = sorted(set(nums), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None

def main_second_largest():
    print("\nFind Second Largest")
    print(second_largest([5, 2, 9, 1]))
    print(second_largest([3, 3, 3]))
    print(second_largest([8]))

# -------------------- Check Anagram --------------------
def is_anagram(s1: str, s2: str):
    """Checks if two strings are anagrams."""
    return sorted(s1.lower()) == sorted(s2.lower())

def main_check_anagram():
    print("\nCheck Anagram")
    print(is_anagram("listen", "silent"))
    print(is_anagram("apple", "pale"))

# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    main_multiplication_table()
    main_swap_numbers()
    main_check_substring()
    main_decimal_to_bin()
    main_matrix_add()
    main_matrix_multiply()
    main_second_largest()
    main_check_anagram()

# AI-BASED TIC-TAC-TOE
import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_winner = None  # Track the winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        
        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # X starts first
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')  # empty line

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('It\'s a tie!')

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{self.letter}\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = 4  # Start with center if empty
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # AI is maximizing player
        other_player = 'O' if player == 'X' else 'X'

        # Base cases
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player 
                    else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # Recursive case
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Maximize
        else:
            best = {'position': None, 'score': math.inf}  # Minimize

        for possible_move in state.available_moves():
            # Make move
            state.make_move(possible_move, player)
            
            # Simulate game after move
            sim_score = self.minimax(state, other_player)
            
            # Undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            
            sim_score['position'] = possible_move
            
            if player == max_player:  # Maximizing player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:  # Minimizing player
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = AIPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

def main_tic_tac_toe():
    print("\nAI-Based Tic-Tac-Toe")
    x_player = HumanPlayer('X')
    o_player = AIPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
    
main_tic_tac_toe()