import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the expression: 4 divided by 5
result = mp.mpf(4) / mp.mpf(5)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))