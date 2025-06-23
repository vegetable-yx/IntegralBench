import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is a constant: 626
result = mp.mpf(626)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))