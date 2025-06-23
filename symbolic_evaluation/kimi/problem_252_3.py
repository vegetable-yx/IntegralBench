import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 8 to get final result
result = mp.fdiv(pi_squared, 8)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))