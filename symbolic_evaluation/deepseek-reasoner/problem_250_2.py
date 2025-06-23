import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute (sqrt(2) - 1)
difference = sqrt2 - 1

# Multiply by pi to get final result
result = difference * mp.pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))