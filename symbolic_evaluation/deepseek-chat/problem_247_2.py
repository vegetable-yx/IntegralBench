import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the expression: 1/32
numerator = mp.mpf(1)
denominator = mp.mpf(32)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))