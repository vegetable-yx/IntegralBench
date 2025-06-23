import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute the analytical expression: 4/5
result = mp.mpf(4) / mp.mpf(5)

# Output the result to 10 decimal places
print(mp.nstr(result, n=10))