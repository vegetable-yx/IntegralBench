import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the result: -3 times pi
result = -3 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))