import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Numerator of the fraction
numerator = mp.mpf(5)

# Denominator of the fraction
denominator = mp.mpf(6)

# Compute the result by division
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))