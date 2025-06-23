import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Define numerator and denominator using arbitrary-precision floats
numerator = mp.mpf(8)
denominator = mp.mpf(7)

# Perform exact rational division with mpmath
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))