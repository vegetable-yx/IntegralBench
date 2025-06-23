import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = 80
denominator = 23

# Compute the fraction 80/23
fraction_val = mp.mpf(numerator) / mp.mpf(denominator)

# Compute natural logarithm of the fraction
result = mp.log(fraction_val)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))