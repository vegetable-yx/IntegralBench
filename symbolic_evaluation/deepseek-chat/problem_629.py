import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Define numerator and denominator
numerator = 253
denominator = 3

# Calculate the fraction 253/3 using mpmath types
fraction = mp.mpf(numerator) / mp.mpf(denominator)

# Compute natural logarithm of the fraction
result = mp.log(fraction)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))