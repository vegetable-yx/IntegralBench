import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate numerator and denominator
numerator = 2023
denominator = 2022

# Compute the exact fraction using arbitrary precision
result = -mp.mpf(numerator) / mp.mpf(denominator)

# Print result with 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))