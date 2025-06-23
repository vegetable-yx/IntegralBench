import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Step 1: Retrieve the constant π
pi_val = mp.pi

# Step 2: Compute π squared
pi_squared = pi_val ** 2

# Step 3: Divide by 2 to obtain the result
result = pi_squared / 2

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))