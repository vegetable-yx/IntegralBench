import mpmath as mp
mp.dps = 15  # Set internal decimal places for calculations

# Define numerator and denominator using mpmath types
numerator = mp.mpf(1)
denominator = mp.mpf(5)

# Perform exact rational division using mpmath
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))