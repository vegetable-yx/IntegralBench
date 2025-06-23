import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute pi constant
pi_val = mp.pi

# Step 2: Square pi
pi_squared = pi_val ** 2

# Step 3: Divide by 4 to get final result
result = pi_squared / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))