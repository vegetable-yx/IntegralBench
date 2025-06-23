import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate pi value using mpmath's constant
pi_value = mp.pi

# Compute pi cubed
pi_cubed = pi_value ** 3

# Divide by 8 to get final result
result = pi_cubed / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))