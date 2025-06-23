import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the constant e (base of natural logarithm)
e = mp.e

# Calculate 1/e
inv_e = 1 / e

# Compute the term (1 - 1/e)
term = 1 - inv_e

# Multiply by pi/2
result = (mp.pi / 2) * term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))