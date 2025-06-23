import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Step 1: Get the constant π
pi_val = mp.pi

# Step 2: Compute π raised to the third power
pi_cubed = pi_val ** 3

# Step 3: Divide the result by 4 to get the final value
result = pi_cubed / 4

# Print the result with exactly 10 significant digits
print(mp.nstr(result, n=10))