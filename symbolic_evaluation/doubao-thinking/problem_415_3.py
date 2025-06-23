import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the exact fraction: 4 divided by 5
numerator = 4
denominator = 5
result = mp.mpf(numerator) / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))