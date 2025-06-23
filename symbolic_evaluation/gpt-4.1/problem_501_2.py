import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the fraction 2/5
result = mp.mpf(2) / mp.mpf(5)

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))