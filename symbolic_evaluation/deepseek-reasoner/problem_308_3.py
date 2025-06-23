import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute the analytical expression pi/3
result = pi_value / 3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))