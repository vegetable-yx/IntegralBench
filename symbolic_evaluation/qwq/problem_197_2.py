import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the result: 1/4
result = mp.mpf(1) / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))