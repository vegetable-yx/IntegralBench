import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi value
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide by 12 to get final result
result = pi_cubed / 12

# Print result with 10 decimal places
print(mp.nstr(result, n=10))