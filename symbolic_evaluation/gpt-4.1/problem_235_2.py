import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant: 8
result = mp.mpf(8)

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))