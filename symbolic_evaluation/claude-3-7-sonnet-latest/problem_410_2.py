import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the constant e (base of natural logarithm)
e_const = mp.e

# Compute denominator: 2 multiplied by e
denominator = 2 * e_const

# Compute final result: sqrt(pi) divided by (2e)
result = sqrt_pi / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))