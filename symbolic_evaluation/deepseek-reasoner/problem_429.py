import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate numerator and denominator as precise floating-point numbers
numerator = mp.mpf(80)
denominator = mp.mpf(23)

# Compute the ratio of 80/23 with full precision
fraction = numerator / denominator

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))