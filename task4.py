# Task 25: Find Missing Number
def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example
arr = [1, 2, 4, 5, 6]
print("Missing number:", find_missing_number(arr))


# Task 26: Check Balanced Parentheses
def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# Example
s = "{[()()]}"
print("Is balanced:", is_balanced(s))


# Task 27: Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example
sentence = "Find the longest word in this sentence"
print("Longest word:", longest_word(sentence))


# Task 28: Count Words in a Sentence
def count_words(sentence):
    return len(sentence.split())

# Example
sentence = "Count the number of words in this sentence"
print("Word count:", count_words(sentence))


# Task 29: Check Pythagorean Triplet
def is_pythagorean_triplet(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Example
a, b, c = 3, 4, 5
print("Is Pythagorean triplet:", is_pythagorean_triplet(a, b, c))


# Task 30: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))


# Task 31: Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print("Target index:", binary_search(arr, target))


# Task 32: Find Subarray with Given Sum
def find_subarray_with_sum(arr, target_sum):
    n = len(arr)
    for i in range(n):
        current_sum = arr[i]
        if current_sum == target_sum:
            return [i, i]
        for j in range(i + 1, n):
            current_sum += arr[j]
            if current_sum == target_sum:
                return [i, j]
    return -1

# Example
arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
print("Subarray indices:", find_subarray_with_sum(arr, target_sum))


# Task 4: Log Analysis System
from collections import Counter

def log_analysis(log_file):
    ip_counter = Counter()
    status_counter = Counter()
    url_counter = Counter()

    with open(log_file, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 7:
                ip = parts[0]
                status = parts[8]
                url = parts[6]
                ip_counter[ip] += 1
                status_counter[status] += 1
                url_counter[url] += 1

    print("Most frequent IP addresses:", ip_counter.most_common(5))
    print("Most frequent status codes:", status_counter.most_common(5))
    print("Most frequent URLs:", url_counter.most_common(5))

# Example usage (ensure you have a valid log file)
log_file = 'server_log.txt'  # Replace with your actual log file
# log_analysis(log_file)  # Uncomment to run log analysis
