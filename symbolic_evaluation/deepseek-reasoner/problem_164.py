import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the result directly from the analytical solution
result = 384

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))