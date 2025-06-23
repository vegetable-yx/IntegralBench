import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide by 8 to get final result
result = pi_squared / 8

# Print result with 10 decimal places
print(mp.nstr(result, n=10))