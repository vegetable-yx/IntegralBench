import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the fraction 253/3
fraction = mp.mpf(253) / mp.mpf(3)

# Calculate the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))