import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the calculated π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 32
result = mp.fdiv(pi_squared, 32)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))