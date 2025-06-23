import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Step 1: Compute the constant pi
pi_value = mp.pi

# Step 2: Subtract 2 from pi
result = pi_value - 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))