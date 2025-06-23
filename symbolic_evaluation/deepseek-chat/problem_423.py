import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# The analytical expression is the constant 99
result = mp.mpf(99)

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))