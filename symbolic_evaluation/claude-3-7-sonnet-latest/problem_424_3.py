import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# The analytical expression is the constant zero
result = mp.mpf(0)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))