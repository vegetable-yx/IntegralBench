import mpmath as mp
mp.dps = 15  # Set decimal precision for all calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = pi_value ** 2

# Divide squared π by 4 to get final result
result = pi_squared / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))