import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the fraction 80/23 with high precision
fraction = mp.mpf(80) / mp.mpf(23)

# Compute natural logarithm of the fraction
result = mp.log(fraction)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))