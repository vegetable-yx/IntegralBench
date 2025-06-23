import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = 5
denominator = 6

# Convert integers to mpmath floating-point numbers
num_mp = mp.mpf(numerator)
den_mp = mp.mpf(denominator)

# Compute the fraction
result = num_mp / den_mp

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))