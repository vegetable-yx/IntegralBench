import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute the square root of 8
sqrt_val = mp.sqrt(8)

# Step 2: Compute the sine of the square root value
sin_val = mp.sin(sqrt_val)

# Step 3: Multiply the sine value by 2
result = 2 * sin_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))