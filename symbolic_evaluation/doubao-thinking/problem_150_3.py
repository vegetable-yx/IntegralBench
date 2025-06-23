import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the value of π
pi_squared = mp.power(pi_value, 2)

# Divide the squared result by 2
result = mp.fdiv(pi_squared, 2)

# Print the final value with 10 decimal places precision
print(mp.nstr(result, n=10))