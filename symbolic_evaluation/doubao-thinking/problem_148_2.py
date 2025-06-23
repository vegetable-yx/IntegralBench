import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 4 to get final result
result = mp.fdiv(pi_squared, 4)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))