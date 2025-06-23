import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# The analytical expression is the constant 5040
result = 5040

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))