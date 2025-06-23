import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the constant e (base of natural logarithm)
e_const = mp.e

# Denominator: 2 multiplied by e
denominator = 2 * e_const

# Final result: sqrt(pi) divided by (2e)
result = sqrt_pi / denominator

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))