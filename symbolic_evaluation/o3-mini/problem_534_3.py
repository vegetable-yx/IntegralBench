import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply by 2 to get the result
result = 2 * sqrt_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))