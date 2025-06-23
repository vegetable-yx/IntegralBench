import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator of the fraction
numerator = 4
denominator = 3

# Convert to mpmath floats and compute the division
num_mp = mp.mpf(numerator)
den_mp = mp.mpf(denominator)
result = num_mp / den_mp

# Print result to 10 decimal places
print(mp.nstr(result, n=10))