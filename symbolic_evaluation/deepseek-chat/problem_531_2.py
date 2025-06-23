import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Define numerator and denominator
numerator = 5
denominator = 6

# Convert integers to mpmath floating-point numbers
num_mp = mp.mpf(numerator)
den_mp = mp.mpf(denominator)

# Compute the exact fraction
result = num_mp / den_mp

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))