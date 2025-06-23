import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate numerator and denominator using mpmath types
numerator = mp.mpf(4)
denominator = mp.mpf(3)

# Perform exact rational division with mpmath
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))