import mpmath as mp
mp.dps = 15

# Define numerator and denominator
numerator = 2023
denominator = 2022

# Calculate the exact fraction using high-precision arithmetic
result = -mp.mpf(numerator) / mp.mpf(denominator)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))