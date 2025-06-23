import mpmath as mp

# Set internal decimal places to 15 for precision
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide by 8 to get the final result
result = pi_cubed / 8

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))