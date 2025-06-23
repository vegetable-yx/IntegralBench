import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the exact value of 4/3
result = mp.mpf(4) / mp.mpf(3)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))