import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# The analytical expression is the constant value 1005
result = mp.mpf(1005)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))