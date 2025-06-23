import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute pi to the fourth power
pi_fourth = mp.pi ** 4

# Step 2: Multiply by 7
term = 7 * pi_fourth

# Step 3: Add 384
result = term + 384

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))