import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the analytical expression: 2 divided by 3
numerator = mp.mpf(2)
denominator = mp.mpf(3)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))