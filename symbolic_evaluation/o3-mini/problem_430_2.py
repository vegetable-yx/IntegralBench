import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = -2023
denominator = 2022

# Convert to mpmath floating-point numbers
num_mp = mp.mpf(numerator)
den_mp = mp.mpf(denominator)

# Compute the fraction
result = num_mp / den_mp

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))