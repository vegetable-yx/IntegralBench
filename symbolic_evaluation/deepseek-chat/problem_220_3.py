import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the constant pi
pi_value = mp.pi

# Compute the square root of 2
sqrt_two = mp.sqrt(2)

# Calculate the result: pi divided by sqrt(2)
result = pi_value / sqrt_two

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))