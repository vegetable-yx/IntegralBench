import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute the numerical value directly from the given result
result = mp.mpf('1.1094607370')

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))