import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Define the mathematical constant pi
pi_val = mp.pi

# Compute the result: negative of pi
result = -pi_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))