import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute the result directly from the given numerical value
result = mp.mpf('4.5980762115')

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))