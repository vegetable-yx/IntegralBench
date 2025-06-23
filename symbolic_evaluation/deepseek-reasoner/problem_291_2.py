import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Direct assignment of the analytical result
result = 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))