import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the argument of the logarithm
fraction = mp.mpf(253) / mp.mpf(3)

# Compute the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))