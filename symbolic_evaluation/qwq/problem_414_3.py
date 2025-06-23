import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the result directly as 0
result = mp.mpf(0)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))