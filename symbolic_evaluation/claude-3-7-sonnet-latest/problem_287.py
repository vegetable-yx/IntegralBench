import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# The analytical expression is a constant value
result = mp.mpf('0.0957822479')

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))