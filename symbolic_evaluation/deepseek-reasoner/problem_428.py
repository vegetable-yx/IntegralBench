import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Direct assignment of the analytical result
result = mp.mpf(17)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))