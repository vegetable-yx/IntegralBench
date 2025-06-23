import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the simple fraction 1/4 using mpmath's arbitrary precision
result = mp.mpf(1)/4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))