import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator with high precision
numerator = mp.mpf(1)
denominator = mp.mpf(4)

# Perform exact division using mpmath types
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))