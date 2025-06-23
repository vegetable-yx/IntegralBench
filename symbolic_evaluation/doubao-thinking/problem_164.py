import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Direct assignment of the exact result
result = mp.mpf(384)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))