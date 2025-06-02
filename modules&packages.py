# Modules
import math
print(math.sqrt(16))

from math import pi
print(pi)

import random
print(random.randint(1, 10))

from datetime import datetime
print(datetime.now())

import os
print('the directory is-',os.getcwd())

import utils
print(utils.greet("Alice"))

#Package
from camelcase import CamelCase
c = CamelCase()
s = 'this is a sentence that needs CamelCasing!'
print (c.hump(s))


# ---------------------------------------PRACTICE EXERCISE---------------------------------------------

# 1) Use the math module to calculate the area of a circle with radius 5
import math
radius = 5
area = math.pi * radius ** 2
print("Area of the circle:", round(area,4))

# 2) Use random to simulate a dice roll (1–6)
import random
dice_roll = random.randint(1, 6)
print("You rolled:", dice_roll)

# 3) Create a custom module with a function that converts Celsius to Fahrenheit
import temp
temp_c = 25
temp_f = temp.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")

# 4) Install the requests package and make a GET request to https://api.github.com
import requests
response = requests.get('https://api.github.com')
print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())

# 5) Use the os module to list all files in the current directory
import os
all_entries = os.listdir()
files = [f for f in all_entries if os.path.isfile(f)]
print("Files in the current directory:")
for file in files:
    print(file)
