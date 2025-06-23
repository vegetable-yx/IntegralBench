import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is the constant 4036
result = mp.mpf(4036)

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))