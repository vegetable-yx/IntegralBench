import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Divide by 8
result = pi_cubed / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))