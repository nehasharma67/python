# 1. Create a function that accepts a list of numbers and returns a new list with only even numbers.

def even_num(numbers):
    return [x for x in numbers if x % 2 == 0]
ip = input("Enter numbers separated by spaces: ")
list1 = []
for item in ip.split():
    list1.append(int(item))
even = even_num(list1)
print("Even numbers:", even)


# 2. Write a program that takes a user’s name and age as input and writes it to a file

name = input("Enter your name: ")
age = input("Enter your age: ")
with open("practice.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
print('written to file')

# 3. Create a program that reads a file and counts how many lines, words, and characters it contains.

file_name = "practice.txt"
with open(file_name, "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)
print(f"File: {file_name}")
print(f"Total lines: {line_count}")
print(f"Total words: {word_count}")
with open(file_name, "r") as file:
           ab=file.read()
           char_count = len(ab)
           print(f"Total characters: {char_count}")


# 4. Build a lambda function that multiplies two numbers and use it with map() to apply it on a list of tuples.

list1 = [(2, 3), (4, 5), (6, 7), (8, 9)]
res = list(map(lambda x: x[0] * x[1], list1))
print(res)

# 5. Write a program using filter() that removes empty strings from a list.

str1 = ["apple", "", "banana", "", "cherry", ""]
non_empty = list(filter( , strings))
print("List after removing empty strings: ", non_empty)

# 6) Create a dictionary of students and their scores, then print names of students who scored above 75.

dict1 = { "Nityaa": 82, "Aditya": 68, "Shitiz": 90, "Deepa": 74, "Sanjoli": 78 }
print("Students who scored above 75:")
for student, score in dict1.items():
    if score > 75:
        print(student,"-",score)
