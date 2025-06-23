import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_val = mp.pi

# Square the π value
pi_squared = mp.power(pi_val, 2)

# Divide by 48 to get the final result
result = mp.fdiv(pi_squared, 48)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))