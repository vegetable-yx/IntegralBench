import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the analytical expression: 1/4
result = mp.mpf(1) / mp.mpf(4)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))