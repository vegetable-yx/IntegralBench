import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Get the constant π
pi_val = mp.pi

# Compute π squared
result = pi_val**2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))