import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply by 2 to get the result
result = 2 * sqrt_pi

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))