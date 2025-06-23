import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the analytical expression
result = mp.mpf(0)  # Direct assignment of zero value

# Print result with 10 decimal places
print(mp.nstr(result, n=10))