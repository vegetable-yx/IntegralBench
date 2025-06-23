import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the constant e (base of natural logarithm)
e_constant = mp.e

# Compute the denominator: 2 * e
denominator = 2 * e_constant

# Compute the final result: sqrt(pi) / (2e)
result = sqrt_pi / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))