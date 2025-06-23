import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the natural logarithm of the fraction 80/23
numerator = mp.mpf(80)
denominator = mp.mpf(23)
fraction = numerator / denominator
result = mp.log(fraction)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))