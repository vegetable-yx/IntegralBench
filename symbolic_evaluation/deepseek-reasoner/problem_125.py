import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the calculated π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 16 to get the final result
result = mp.fdiv(pi_squared, 16)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))