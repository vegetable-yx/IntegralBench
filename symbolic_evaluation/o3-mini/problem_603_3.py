import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is the constant 4
result = mp.mpf(4)

# Print the result to 10 significant digits
print(mp.nstr(result, 10))