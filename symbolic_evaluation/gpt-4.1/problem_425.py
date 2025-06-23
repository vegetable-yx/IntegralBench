import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the fraction: 128 divided by 153
numerator = 128
denominator = 153
result = mp.fdiv(numerator, denominator)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))