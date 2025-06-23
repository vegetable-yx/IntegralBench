import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is simply the constant 1
result = mp.mpf(1)

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))