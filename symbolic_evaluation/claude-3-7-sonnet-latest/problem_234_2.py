import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute 2 * pi
result = 2 * mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))