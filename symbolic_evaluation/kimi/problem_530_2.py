import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the first constant value
a = mp.mpf('1.221441469079183')

# Assign the second constant value
b = mp.mpf('0.881373587019543')

# Compute the sum of the two constants
result = a + b

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))