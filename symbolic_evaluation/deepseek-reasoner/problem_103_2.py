import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 12
result = mp.fdiv(pi_squared, 12)

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))