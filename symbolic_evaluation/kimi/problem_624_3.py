import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the calculated π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 18
result = mp.fdiv(pi_squared, 18)

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))