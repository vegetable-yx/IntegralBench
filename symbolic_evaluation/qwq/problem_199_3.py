import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2 * pi
two_pi = 2 * mp.pi

# Compute the square root of (2 * pi)
result = mp.sqrt(two_pi)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))