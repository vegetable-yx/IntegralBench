import mpmath as mp
mp.dps = 15

from mpmath import mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the numerator and denominator of the fraction
numerator = 2
denominator = 5

# Convert integers to mpmath floating-point numbers
num_mp = mp.mpf(numerator)
den_mp = mp.mpf(denominator)

# Compute the fraction 2/5
result = num_mp / den_mp

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))