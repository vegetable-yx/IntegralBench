import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Divide the squared π by 144
result = mp.fdiv(pi_squared, 144)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))