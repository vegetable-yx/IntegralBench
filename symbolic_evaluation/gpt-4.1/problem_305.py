import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction 1/16
result = mp.mpf(1) / mp.mpf(16)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))