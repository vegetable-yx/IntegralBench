import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant value 2
result = mp.mpf(2)

# Output the result to 10 decimal places
print(mp.nstr(result, n=10))