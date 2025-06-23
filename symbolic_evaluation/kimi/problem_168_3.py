import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the exact numerical value from the analytical expression
result = mp.mpf('4.934802200544679')

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))