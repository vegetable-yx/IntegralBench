import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = -2023
denominator = 2022

# Convert integers to mpmath floating-point numbers
num_mp = mp.mpf(numerator)
den_mp = mp.mpf(denominator)

# Compute the division: -2023 / 2022
result = num_mp / den_mp

# Print result with exactly 10 significant digits
print(mp.nstr(result, n=10))