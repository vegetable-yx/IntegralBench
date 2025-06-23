import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the value of π
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 36
result = mp.fdiv(pi_squared, 36)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))