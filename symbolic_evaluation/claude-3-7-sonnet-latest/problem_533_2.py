import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Numerator
numerator = mp.mpf(8)

# Denominator
denominator = mp.mpf(7)

# Compute the fraction
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))