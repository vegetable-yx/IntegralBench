import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = pi_value ** 2

# Divide squared π by 16 to get final result
result = pi_squared / 16

# Print result with 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))