import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide by 4 to get the final result
result = pi_cubed / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))