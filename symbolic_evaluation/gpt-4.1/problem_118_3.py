import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide by 16 to get final result
result = pi_cubed / 16

# Output result to 10 decimal places
print(mp.nstr(result, n=10))