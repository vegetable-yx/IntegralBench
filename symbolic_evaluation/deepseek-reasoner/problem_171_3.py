import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi cubed value
pi_cubed = pi_val ** 3

# Divide by 192 to get final result
result = pi_cubed / 192

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))