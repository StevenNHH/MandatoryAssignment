# TECH2 mandatory assignment - Part A

# ****** Method 1: using loops  and only the function len() ******

# Given data
data = [1, 2, 3, 4, 5]

# Step 1: Calculate the mean
n = len(data)
sum_data = 0
for number in data:
    sum_data += number
    
mean = sum_data / n

# Step 2: Calculate squared deviations from the mean
sum_squared_deviations = 0
for number in data:
    deviation = number - mean
    squared_deviation = deviation * deviation
    sum_squared_deviations += squared_deviation

# Step 3: Calculate variance
variance = sum_squared_deviations / n

# Step 4: Calculate standard deviation
# Since we cannot use the math.sqrt function, we will calculate the square root manually
# We'll use the exponentiation method for approximation, iteratively
approx_sqrt = variance
for _ in range(10):  # iterate a few times for better accuracy
    approx_sqrt = (approx_sqrt + variance / approx_sqrt) / 2

# The standard deviation is the approximated square root of the variance
standard_deviation = approx_sqrt

# printing list 
print("The original sample includes the numbers: " + str(data)) 

print(f"Method 1: Standard Deviation using loops is: {standard_deviation}")

# ****** Method 2: using sum() and len() ******

# initializing list 
num_list = [1, 2, 3, 4, 5] 

# Standard deviation of list 
# Using sum() + list comprehension 
mean = sum(num_list) / len(num_list) 
variance = sum([((x - mean) ** 2) for x in num_list]) / len(num_list) 
res = variance ** 0.5

# Printing result 
print("Method 2: Standard Deviation using sum & len is: " + str(res)) 

# Method 3: ****** Using the std() from NumPy ******

import numpy as np

#declare the dataset list
dataset = np.array([1, 2, 3, 4, 5])

#calculating standard deviation of the dataset
sd = np.std(dataset)

#display output
print("Method 3: Standard Deviation using NumPy is:", sd)