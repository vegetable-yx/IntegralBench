import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the numerator and denominator separately
numerator = -2023  # Negative sign included
denominator = 2022

# Compute the fraction using mpmath's arbitrary precision
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))