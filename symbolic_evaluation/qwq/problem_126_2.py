import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the π value
pi_squared = mp.power(pi_val, 2)

# Multiply squared π by 2
numerator = mp.mul(pi_squared, 2)

# Divide the result by 5 to get final value
result = mp.div(numerator, 5)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))