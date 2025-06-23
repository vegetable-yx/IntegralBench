import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the value of π
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 2 to get final result
result = mp.fdiv(pi_squared, 2)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))