import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute the analytical expression: 4/5
numerator = mp.mpf(4)
denominator = mp.mpf(5)
result = numerator / denominator

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))