import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Direct assignment of the constant value
result = mp.mpf(2)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))