import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide by 90 to get the final result
result = mp.fdiv(pi_squared, 90)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))