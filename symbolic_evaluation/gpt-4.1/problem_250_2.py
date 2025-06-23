import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Step 2: Subtract 1 from the square root of 2
sqrt2_minus_1 = sqrt2 - 1

# Step 3: Multiply the result by pi
result = sqrt2_minus_1 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))