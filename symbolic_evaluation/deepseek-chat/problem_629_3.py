import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the fraction 253/3
numerator = mp.mpf(253)
denominator = mp.mpf(3)
fraction = numerator / denominator

# Compute natural logarithm of the fraction
result = mp.log(fraction)

# Print result to 10 decimal places
print(mp.nstr(result, n=10))