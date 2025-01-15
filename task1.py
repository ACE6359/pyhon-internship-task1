# Task 1: Sum of Two Numbers
def sum_two_numbers(a, b):
    return a + b

# Examples
print("Sum of 3 and 5:", sum_two_numbers(3, 5))
print("Sum of -2 and 7:", sum_two_numbers(-2, 7))

# Task 2: Odd or Even
def odd_or_even(number):
    return "Even" if number % 2 == 0 else "Odd"

# Examples
print("Number 4 is:", odd_or_even(4))
print("Number 7 is:", odd_or_even(7))

# Task 3: Factorial Calculation
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Examples
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))

# Task 4: Fibonacci Sequence
def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

# Examples
print("First 5 Fibonacci numbers:", fibonacci_sequence(5))
print("First 8 Fibonacci numbers:", fibonacci_sequence(8))

# Task 5: Reverse a String
def reverse_string(s):
    return s[::-1]

# Examples
print("Reversed string of 'hello':", reverse_string("hello"))
print("Reversed string of 'Python':", reverse_string("Python"))

# Task 6: Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# Examples
print("Is 'radar' a palindrome?:", is_palindrome("radar"))
print("Is 'hello' a palindrome?:", is_palindrome("hello"))

# Task 7: Leap Year Check
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Examples
print("Is 2024 a leap year?:", is_leap_year(2024))
print("Is 1900 a leap year?:", is_leap_year(1900))

# Task 8: Armstrong Number Check
def is_armstrong_number(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(digit) ** power for digit in digits)

# Examples
print("Is 153 an Armstrong number?:", is_armstrong_number(153))
print("Is 123 an Armstrong number?:", is_armstrong_number(123))

# Task 9: Custom Encryption-Decryption System
# Example of a simple Caesar cipher for encryption and decryption
def caesar_encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(encrypted_message, shift):
    return caesar_encrypt(encrypted_message, -shift)

# Examples
message = "HelloWorld"
shift = 3
encrypted_message = caesar_encrypt(message, shift)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", caesar_decrypt(encrypted_message, shift))

message = "Python_Programming_by_ace"
shift = 5
encrypted_message = caesar_encrypt(message, shift)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", caesar_decrypt(encrypted_message, shift))
