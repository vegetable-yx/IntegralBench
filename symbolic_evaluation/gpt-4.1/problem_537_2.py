import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# The analytical expression is a constant value of 3
result = 3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))