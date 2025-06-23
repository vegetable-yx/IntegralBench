import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute the numerator (π - 2)
numerator = pi_value - 2

# Divide by 4 to get the final result
result = numerator / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))