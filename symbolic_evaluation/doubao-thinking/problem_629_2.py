import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction 253/3
fraction = mp.mpf(253) / mp.mpf(3)

# Compute the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))