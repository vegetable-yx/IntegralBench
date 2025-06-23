import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide by 24 to get the result
result = pi_cubed / 24

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))