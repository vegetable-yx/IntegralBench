import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi and then by -3
result = -3 * mp.pi * sqrt2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))