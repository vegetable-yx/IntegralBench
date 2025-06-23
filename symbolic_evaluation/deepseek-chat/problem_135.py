import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the numerator: 3 * pi
numerator = 3 * mp.pi

# Divide the numerator by 4 to obtain the result
result = numerator / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))