import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Define numerator and denominator
numerator = 128
denominator = 153

# Compute the exact fraction
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))