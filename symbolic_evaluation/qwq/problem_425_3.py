import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Define numerator and denominator
numerator = 128
denominator = 153

# Perform exact division using mpmath types
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))