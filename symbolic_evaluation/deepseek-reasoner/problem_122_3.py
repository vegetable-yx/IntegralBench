import mpmath as mp
mp.dps = 15  # Set internal decimal places for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 4
result = mp.fdiv(pi_squared, 4)

# Output the final result with 10 decimal precision
print(mp.nstr(result, n=10))