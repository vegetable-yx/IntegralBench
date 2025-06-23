import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute sin(1) radians
result = mp.sin(1)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))