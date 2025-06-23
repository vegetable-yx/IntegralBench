import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the value of π
pi_squared = pi_val ** 2

# Divide by 6 to get the final result
result = pi_squared / 6

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))