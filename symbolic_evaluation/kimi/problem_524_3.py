import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Step 1: Compute the square of Euler's number (e^2)
e_squared = mp.e ** 2

# Step 2: Add 1 to e_squared
numerator = e_squared + 1

# Step 3: Divide the numerator by 4 to get the final result
result = numerator / 4

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))