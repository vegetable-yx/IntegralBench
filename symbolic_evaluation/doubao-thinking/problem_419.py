import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide by 6 to get the final result
result = mp.fdiv(pi_squared, 6)

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))