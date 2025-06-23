import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the fraction 3/253 with high precision
numerator = mp.mpf(3)
denominator = mp.mpf(253)
fraction_value = numerator / denominator

# Compute natural logarithm of the fraction
result = mp.log(fraction_value)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))