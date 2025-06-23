import mpmath as mp

# Set the internal decimal precision to 15 to ensure accuracy
mp.dps = 15

# Step 1: Calculate the square root of 8
sqrt8 = mp.sqrt(8)

# Step 2: Add 3 to the square root of 8
three_plus_sqrt8 = 3 + sqrt8

# Step 3: Calculate the square of pi
pi_squared = mp.pi ** 2

# Step 4: Multiply the result from Step 2 by the square of pi
numerator = three_plus_sqrt8 * pi_squared

# Step 5: Divide the numerator by 32 to get the final result
result = numerator / 32

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))