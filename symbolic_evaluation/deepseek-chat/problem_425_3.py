import mpmath as mp

# Set the internal decimal precision to 15 for calculations
mp.dps = 15

# Define the numerator and denominator
numerator = 128
denominator = 153

# Compute the result by dividing numerator by denominator
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))