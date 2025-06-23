import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate numerator and denominator as arbitrary-precision floats
numerator = mp.mpf(-2023)
denominator = mp.mpf(2022)

# Perform exact rational division with mpmath
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))