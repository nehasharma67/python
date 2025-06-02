class Person:
    pass
p1 = Person()
print(p1)

class Dog:
    def bark(self):
        print("Woof! Woof!")

my_dog = Dog()
my_dog.bark()

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
my_car = Car("Toyota", 2022)
print(my_car.brand, my_car.year)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Student: {self.name}, Grade: {self.grade}")
s1 = Student("Alice", "A")
s2 = Student("Bob", "B")
s1.display()
s2.display()

# --------------------------------------------------PRACTICE EXERCISE---------------------------------------------------------

# 1) Create a class called Book with attributes title and author. Add a method to display them
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")
book1 = Book("1984", "George")
book1.display()

# 2) Define a class Circle with a radius attribute and a method to calculate area
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print(f"Area of Circle: {circle.area():.2f}")

# 3) Create a class Employee with attributes name and salary. Add a method to display salary with a bonus (10%)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def bonus(self):
        bonus = self.salary * 0.10
        total_salary = self.salary + bonus
        print(f"Employee Name: {self.name}")
        print(f"Salary with 10% Bonus: {total_salary:.2f}")
name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
employee = Employee(name, salary)
employee.bonus()

# 4) Make a class BankAccount with deposit() and withdraw() methods and balance tracking
class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, Balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Balance: {self.balance}")
        else:
            print("Insufficient balance.")
account = BankAccount()
deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amount)

# 5) Build a class Rectangle that accepts length and width, and returns area and perimeter
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rectangle = Rectangle(length, width)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")


