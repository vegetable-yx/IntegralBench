import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Define the constant factor
factor = mp.mpf(4)

# Retrieve the value of pi from mpmath
pi_value = mp.pi

# Multiply to compute 4 * pi
result = factor * pi_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))