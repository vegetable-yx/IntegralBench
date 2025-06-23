import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Direct assignment of the exact solution
result = mp.mpf(2)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))