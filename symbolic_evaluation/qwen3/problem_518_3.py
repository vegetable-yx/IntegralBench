import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the analytical result directly
result = mp.mpf(4036)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))