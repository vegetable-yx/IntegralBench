import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply by 2 to get the result
result = 2 * sqrt_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))