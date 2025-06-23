import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the fraction 80/23
fraction = mp.mpf(80) / mp.mpf(23)

# Calculate the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))