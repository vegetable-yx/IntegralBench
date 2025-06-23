import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate numerator and denominator
numerator = 4
denominator = 5

# Perform exact division using mpmath types
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))