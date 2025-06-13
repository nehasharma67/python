'''MINI PROJECT: Data Analysis with NumPy

→ Step 1: Generate random student marks
→ Step 2: Calculate average, max, min

Task 1: Find Top 5 Scores
Task 2: Count Students Scoring Above 50
Task 3: Reshape and Analyze Data
Task 4: Simulate 1000 Coin Flips
'''

import numpy as np
marks = np.random.randint(0, 101, size=30)
print('\nMarks are: ',marks,'\n')

print("Average: ",round(np.mean(marks),2) , ", Max: ",np.max(marks) , ", Min: ",np.min(marks) , '\n')

print("Top 5 scores: ",np.sort(marks)[-5: ],'\n')

print("Students scoring above 50: ", np.sum(marks > 50),'\n')

reshaped = marks.reshape(6, 5) 
print('Reshaped Array:') 
print(reshaped,'\n')

row_avg = np.mean(reshaped, axis=1)
print('Analysing Data:') 
print(f"Row averages: {row_avg}")
print("Students scoring below 35(FAIL):", np.sum(marks < 35),'\n')

flips = np.random.randint(0, 2, size=1000)
heads = np.sum(flips == 0)
tails = np.sum(flips == 1)
print('Among 1000 Coin Flips:')
print(f"Heads: {heads}, Tails: {tails}")


