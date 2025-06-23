import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the exact value: 1 divided by 12
result = mp.mpf(1) / 12

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))