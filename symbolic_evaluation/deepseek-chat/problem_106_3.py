import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Retrieve the constant π
pi_val = mp.pi

# Step 2: Compute π divided by 2
result = pi_val / 2

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))