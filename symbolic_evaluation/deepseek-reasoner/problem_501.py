import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Define numerator and denominator using mpmath types
numerator = mp.mpf(2)
denominator = mp.mpf(5)

# Perform exact rational division with mpmath
result = numerator / denominator

# Output result with exactly 10 decimal places
print(mp.nstr(result, n=10))