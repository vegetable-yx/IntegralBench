import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction 8/3
numerator = 8
denominator = 3
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))