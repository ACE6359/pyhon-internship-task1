#question 9:

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(6))
print(is_prime(35))
print(is_prime(11))
print(is_prime(31))

#question 10:

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n))) 
print(sum_of_digits(456))
print(sum_of_digits(14686))

#question 11:

import math
def lcm_and_gdc(a, b):
    gdc = math.gcd(a, b)
    lcm = abs(a*b)// gdc
    return lcm, gdc
print(lcm_and_gdc(22, 14))
print(lcm_and_gdc(12, 18))

#question 12:

def reverse_list(lst):
    reversed_lst =[]
    for i in range(len(lst) -1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
print(reverse_list([1, 5, 8, 9]))
print(reverse_list([4, 48, 96, 105]))

#question 13:

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1],lst[j]
    return lst
print(bubble_sort([4,5,8,12,45,12,25]))
print(bubble_sort([4,25,3,6,5,89,7,20,45,4,-4,-5,-1,-45]))

#question 14:

def remove_duplicates(lst):
    unique_elements = []
    for item in lst:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements
print(remove_duplicates([1, 1, 25, 25, 2, 2, 6, 6, 25, 85, 65, 3, 85, 65]))

#question 15:

def string_length(s):
    length = 0
    for _ in s:
        length += 1
    return length
print(string_length("hi iam shiva"))
print(string_length("my age is twenty one"))

#question 16:

def count_vowels_and_constants(s):
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    vowel_count = consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
print(count_vowels_and_constants("hello iam shiva alias ace"))
print(count_vowels_and_constants("153163asce"))

#question 17:

import random

def generate_maze(rows, cols):
    maze = [[1 if random.random() < 0.3 else 0 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = maze[rows-1][cols-1] = 0
    return maze
def print_maze(maze):
    for row in maze:
        print(''.join('█' if cell == 1 else ' ' for cell in row))

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range (cols)] for _ in range(rows)]
    path = []
    
    def dfs(x, y):
        if x < 0 or y < 0 or x >= rows or y >= cols or maze[x][y] == 1 or visited[x][y]:
            return False
        visited[x][y] = True
        path.append((x, y))
        if (x, y) == (rows-1, cols-1):
            return True
        if dfs(x+1, y) or dfs(x, y+1) or dfs(x-1, y) or dfs(x, y-1):
            return True
        path.pop()
        return False
    
    dfs(0, 0)
    return path

maze = generate_maze(5, 5)
print("maze:")
print_maze(maze)
solution = solve_maze(maze)
print("path to exit:", solution) 