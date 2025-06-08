# 1. Reverse Each Word in a Sentence
def rev(sentence):
    return ' '.join(word[::-1] for word in sentence.split())
user_input = input("Enter a sentence: ")
result = rev(user_input)
print("Output:", result)

# 2. Count Files by Extension
def count_files_by_extension(filenames):
    extension_count = {}
    for file in filenames:
        if '.' in file:
            ext = file.rsplit('.', 1)[-1]
            extension_count[ext] = extension_count.get(ext, 0) + 1
        else:
            extension_count['no_extension'] = extension_count.get('no_extension', 0) + 1
    return extension_count
user_input = input("Enter filenames separated by space: ")
file_list = user_input.split()
result = count_files_by_extension(file_list)
print("Extension Counts:", result)

# 3. Remove Consecutive Duplicates
def remove_consecutive_duplicates(s):
    if not s:
        return ""
    for char in s[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)
user_input = input("Enter a string: ")
output = remove_consecutive_duplicates(user_input)
print("Output:", output)


# 4. Find Missing Number in a Sequence
def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum
user_input = input("Enter the list of numbers from 1 to n with one missing (space-separated): ")
numbers = list(map(int, user_input.split()))
n = int(input("Enter the value of n (the range should be 1 to n): "))
missing_number = find_missing_number(numbers, n)
print("Missing Number:", missing_number)

# 5. Count Vowels and Consonants
def count_vowels_and_consonants(s):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    for char in s.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
user_input = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(user_input)
print("Vowels:", vowels)
print("Consonants:", consonants)

# 6. Group Words by Anagram
from collections import defaultdict
def group_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        anagram_dict[key].append(word)
    return list(anagram_dict.values())
user_input = input("Enter words separated by space: ")
word_list = user_input.split()
result = group_anagrams(word_list)
print("Grouped Anagrams:")
for group in result:
    print(group)

# 7. Flatten a Nested List
def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item)) 
        else:
            flat.append(item)
    return flat
user_input = input("Enter a nested list (e.g., [1, [2, [3, [4]]]]): ")
nested_list = eval(user_input)
result = flatten_list(nested_list)
print("Flattened List:", result)

# 8. Frequency of Elements
def frequency_count(lst):
    freq = {}
    for elem in lst:
        freq[elem] = freq.get(elem, 0) + 1
    return freq
user_input = input("Enter elements separated by space: ")
elements = user_input.split()
freq_dict = frequency_count(elements)
print("Frequency using loop:", freq_dict)

# 9. Check for Palindrome Ignoring Non-Alphanumeric
def is_palindrome(s):
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    return filtered_chars == filtered_chars[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome (ignoring non-alphanumeric characters).")
else:
    print("The string is NOT a palindrome.")

# 10. Sort Dictionary by Value
def sort_dict_by_value(d):
    sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items)
user_input = input("Enter dictionary items (key:value) separated by space: ")
input_dict = {}
for pair in user_input.split():
    key, value = pair.split(':')
    try:
        value = int(value)
    except ValueError:
        pass
    input_dict[key] = value
sorted_dict = sort_dict_by_value(input_dict)
print("Sorted Dictionary by Value (descending):", sorted_dict)

# 11. Custom Sorting Function
def custom_sort(lst):
    return sorted(lst, key=lambda x: (-x[1], x[0]))
user_input = input("Enter name and age pairs separated by commas (e.g., John 25, Alice 30): ")
pairs = []
for item in user_input.split(','):
    name_age = item.strip().split()
    if len(name_age) == 2:
        name, age_str = name_age
        try:
            age = int(age_str)
            pairs.append((name, age))
        except ValueError:
            print(f"Invalid age value: {age_str}, skipping this entry.")
    else:
        print(f"Invalid input format for entry: '{item.strip()}', skipping.")
sorted_pairs = custom_sort(pairs)
print("Sorted list:")
for name, age in sorted_pairs:
    print(f"{name} {age}")

# 12. Implement a Decorator to Time Function Execution
import time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()       
        result = func(*args, **kwargs) 
        end_time = time.time()         
        elapsed = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed:.6f} seconds.")
        return result
    return wrapper
@timer_decorator
def example_function(seconds):
    time.sleep(seconds)
    return f"Slept for {seconds} seconds."
secs = float(input("Enter seconds to sleep: "))
output = example_function(secs)
print(output)

# 13. Rotate Matrix by 90 Degrees
def rotate_90_clockwise(matrix):
    transposed = list(zip(*matrix))
    rotated = [list(row[::-1]) for row in transposed]
    return rotated
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter the matrix rows, each element separated by space:")
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    if len(row) != cols:
        print("Invalid number of elements in row, please enter again.")
        exit()
    matrix.append(row)
rotated_matrix = rotate_90_clockwise(matrix)
print("Matrix after 90 degree clockwise rotation:")
for row in rotated_matrix:
    print(*row)

# 14. Validate Password Strength
import string
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(ch.isupper() for ch in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(ch.isdigit() for ch in password):
        return False, "Password must contain at least one digit."
    special_chars = set(string.punctuation)
    if not any(ch in special_chars for ch in password):
        return False, "Password must contain at least one special character."
    return True, "Password is strong."
pwd = input("Enter a password to validate: ")
is_valid, message = validate_password(pwd)
print(message)

# 15. Implement a Generator for Prime Numbers
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
def prime_generator(n):
    for number in range(2, n):
        if is_prime(number):
            yield number
limit = int(input("Generate primes less than: "))
print(f"Prime numbers less than {limit}:")
for prime in prime_generator(limit):
    print(prime, end=' ')
print()
