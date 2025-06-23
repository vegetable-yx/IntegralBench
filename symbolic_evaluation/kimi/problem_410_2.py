import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the numerator: square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the denominator: 2 multiplied by Euler's number
denominator = 2 * mp.e

# Compute the final result by dividing numerator by denominator
result = sqrt_pi / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))