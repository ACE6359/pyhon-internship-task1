from itertools import permutations
from collections import Counter
import heapq
import random

# Task 33: Find All Permutations of a String
def find_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Example 1
print(find_permutations("abc"))
# Example 2
print(find_permutations("xyz"))

# Task 34: N-th Fibonacci Number
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example 1
print(fibonacci(8))
# Example 2
print(fibonacci(12))

# Task 34: Find Duplicates in a List
def find_duplicates(lst):
    counter = Counter(lst)
    return [num for num, count in counter.items() if count > 1]

# Example 1
print(find_duplicates([1, 1, 2, 3, 4, 5, 6, 2]))
# Example 2
print(find_duplicates([7, 8, 8, 9, 10, 11, 11]))

# Task 35: Longest Increasing Subsequence
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example 1
print(longest_increasing_subsequence([1, 3, 5, 2, 8, 6, 7]))
# Example 2
print(longest_increasing_subsequence([4, 10, 6, 8, 11, 15]))

# Task 36: Find K Largest Elements
def find_k_largest(lst, k):
    return heapq.nlargest(k, lst)

# Example 1
print(find_k_largest([9, 2, 5, 4, 6, 8], 3))
# Example 2
print(find_k_largest([12, 1, 4, 7, 10], 2))

# Task 37: Rotate Matrix
def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

# Example 1
print(rotate_matrix([[1, 2], [3, 4]]))
# Example 2
print(rotate_matrix([[5, 6, 7], [8, 9, 10], [11, 12, 13]]))

# Task 38: Sudoku Validator
def is_valid_sudoku(board):
    def is_valid_group(group):
        group = [num for num in group if num != '.']
        return len(group) == len(set(group))
    
    for row in board:
        if not is_valid_group(row):
            return False
    
    for col in zip(*board):
        if not is_valid_group(col):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_group(block):
                return False
    
    return True

# Example 1
sudoku_board_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "2"],
    ["6", ".", ".", "1", "9", "5", ".", ".", "8"],
    [".", "9", "8", ".", ".", ".", ".", "6", "3"],
    ["8", ".", ".", ".", "6", ".", "1", ".", "3"],
    ["4", "2", ".", "8", ".", "3", ".", ".", "1"],
    ["7", "6", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", "3", ".", ".", ".", "2", "8", "."],
    [".", "1", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", "2", ".", "8", ".", ".", "7", "9"]]
print(is_valid_sudoku(sudoku_board_1))

# Task: Virtual Stock Market Simulator
class StockMarket:
    def __init__(self):
        self.stocks = {"AAPL": 150, "GOOGL": 2800, "TSLA": 700}
        self.portfolio = {}
    
    def buy_stock(self, stock, quantity):
        if stock in self.stocks:
            cost = self.stocks[stock] * quantity
            self.portfolio[stock] = self.portfolio.get(stock, 0) + quantity
            return f"Bought {quantity} shares of {stock} for ${cost}"
        return "Stock not available"
    
    def sell_stock(self, stock, quantity):
        if stock in self.portfolio and self.portfolio[stock] >= quantity:
            self.portfolio[stock] -= quantity
            revenue = self.stocks[stock] * quantity
            return f"Sold {quantity} shares of {stock} for ${revenue}"
        return "Not enough shares to sell"
    
    def update_prices(self):
        for stock in self.stocks:
            self.stocks[stock] += random.randint(-10, 10)

# Example 1
market = StockMarket()
print(market.buy_stock("AAPL", 10))
market.update_prices()
print(market.sell_stock("AAPL", 5))

# Example 2
market = StockMarket()
print(market.buy_stock("GOOGL", 2))
market.update_prices()
print(market.sell_stock("GOOGL", 1))                                                                                                    
