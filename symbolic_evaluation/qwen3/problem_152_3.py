import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the value of π
pi_squared = mp.power(pi_value, 2)

# Divide the squared result by 2
result = mp.fdiv(pi_squared, 2)

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))