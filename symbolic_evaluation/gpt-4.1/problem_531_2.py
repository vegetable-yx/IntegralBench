import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Define numerator and denominator
numerator = 5
denominator = 6

# Compute the fraction 5/6
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))