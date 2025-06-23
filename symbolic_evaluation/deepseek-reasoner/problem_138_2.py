import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Direct assignment of the analytical result
result = 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))