import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi value
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide by 8 to get the result
result = pi_cubed / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))