import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the exact value: 4 divided by 3
numerator = mp.mpf(4)
denominator = mp.mpf(3)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))