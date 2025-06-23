import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the value of π
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 8 to get the final result
result = mp.fdiv(pi_squared, 8)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))