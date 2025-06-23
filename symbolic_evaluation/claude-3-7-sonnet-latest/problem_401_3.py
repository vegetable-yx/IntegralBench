import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the result: 1 divided by 2
result = mp.mpf(1) / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))