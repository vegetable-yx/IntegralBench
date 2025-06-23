import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Compute the constant e (base of natural logarithm)
e_constant = mp.e

# Subtract 2 from e
result = e_constant - 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))