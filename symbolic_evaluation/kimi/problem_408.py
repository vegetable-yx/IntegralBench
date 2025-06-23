import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate numerator and denominator as mpf objects
numerator = mp.mpf(1)
denominator = mp.mpf(24)

# Perform exact division using mpmath types
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))