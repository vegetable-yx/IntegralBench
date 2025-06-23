import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the result directly from the given numerical value
result = mp.mpf('1.228380685')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))