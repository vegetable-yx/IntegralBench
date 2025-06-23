import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the exact value of 8/7
numerator = mp.mpf(8)
denominator = mp.mpf(7)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))