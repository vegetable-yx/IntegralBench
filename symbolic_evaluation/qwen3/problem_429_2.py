import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the fraction 80/23 with high precision
numerator = mp.mpf(80)
denominator = mp.mpf(23)
fraction = numerator / denominator

# Compute natural logarithm of the fraction
result = mp.log(fraction)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))