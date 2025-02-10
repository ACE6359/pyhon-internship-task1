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
